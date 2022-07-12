import json, jwt

from unittest.mock import patch, MagicMock

from django.conf   import settings
from django.test                     import Client
from rest_framework.test             import APITestCase
from users.models  import *

class KakaoSignInTest(APITestCase):
    def setUp(self):
        user = User.objects.create(
            social_id      = "123123",
            nickname      = "test",
            email         = "test@gmail.com",
            profile_image = "https://ifh.123123/g/ElNIU1.jpg",
        )

    def tearDown(self):
        User.objects.all().delete()
    
class SignInTest(APITestCase):
    @patch('users.kakao.requests')
    def test_kakao_signin_view_get_success(self, mocked_requests):
            client = Client()

            class MockedResponse:
                status_code = 200
                
                def json(self):
                    return {
                        "id": 2145645622,
                        "connected_at": "2022-02-16T05:48:20Z",
                        "properties": {
                            "nickname": "test"
                        },
                        "kakao_account": {
                        "profile_nickname_needs_agreement": False,
                        "profile_image_needs_agreement": True,
                        "properties": {
                            "nickname": "test",
                            "thumbnail_image_url": "h123.jpg",
                            "profile_image_url": "h123.jpg",
                            "is_default_image": True
                        },
                        "has_email": True,
                        "email_needs_agreement": False,
                        "is_email_valid": True,
                        "is_email_verified": True,
                        "email": "test@gmail.com",
                        "has_gender": True,
                        }
                    }

            mocked_requests.get = MagicMock(return_value = MockedResponse())
            headers = {"HTTP_Authorization" : "123123"}
            response = client.get("/users/kakao/login/", **headers)

            self.assertEqual(response.status_code, 200) 
            
    @patch('users.kakao.requests')
    def test_kakao_signin_fail_key_error(self, mocked_requests):
        client = Client()
        
        class MockedResponse:
            status_code = 400

            def json(self):
                return {
                    'id' : 2145645622,
                    'kakao_account' : {
                        'profile' : {
                            'nickname' : 'test'
                        }
                    }
                }
        
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {'Authorization' : '123123'}
        response            = client.get('/users/kakao/login/', **headers)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'Key error'})
