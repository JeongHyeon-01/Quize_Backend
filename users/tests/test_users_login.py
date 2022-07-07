from unittest.mock import patch, MagicMock

from rest_framework.test import APITestCase, DjangoClient

from users.models  import *

client = DjangoClient()

class UserSignInTest(APITestCase):
    def setUp(self):
        user = User.objects.create(
            id       = "1",
            uid      = '123123123',
            username = "test",
            email    = "test@gmail.com",
            picture  = "https://ifh.123123/g/ElNIU1.jpg",
        )

    def tearDown(self):
        User.objects.all().delete()

    @patch('users.views.requests')
    def test_fist_time_user_login_success(self, mocked_requests):

        class MockedResponse:
            status_code = 200
            
            def json(self):
                return   {
                    'iss'           : '123123',
                    'nbf'           : '123123123',
                    'aud'           : '123123',
                    'sub'           : '34563456345',
                    'email'         : '123@gmail.com',
                    'email_verified': '123',
                    'azp'           : '1123',
                    'name'          : 'test',
                    'picture'       : 'test',
                    'given_name'    : 'test',
                    'family_name'   : 'test',
                    'iat'           : '123123',
                    'exp'           : '123123',
                    'jti'           : '123123',
                    'alg'           : 'RS256',
                    'kid'           : '2650a2ce47b1ab3ba4099797f8c06ebc3de928ac',
                    'typ'           : 'JWT'
                    }
                
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {"HTTP_Authorization" : "123123"}
        response            = client.get("/users/login/", **headers)
        self.assertEqual(response.status_code, 200)

    @patch('users.views.requests')
    def test_exists_user_login_success(self, mocked_requests):

        class MockedResponse:
            status_code = 200

            def json(self):
                return   {
                    'iss'           : '123123',
                    'nbf'           : '123123123',
                    'aud'           : '123123',
                    'sub'           : '123123',
                    'email'         : '123@gmail.com',
                    'email_verified': '123',
                    'azp'           : '1123',
                    'name'          : 'test',
                    'picture'       : 'test',
                    'given_name'    : 'test',
                    'family_name'   : 'test',
                    'iat'           : '123123',
                    'exp'           : '123123',
                    'jti'           : '123123',
                    'alg'           : 'RS256',
                    'kid'           : '2650a2ce47b1ab3ba4099797f8c06ebc3de928ac',
                    'typ'           : 'JWT'
                    }

        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {"HTTP_Authorization" : "123123"}
        response            = client.get("/users/login/", **headers)
        self.assertEqual(response.status_code, 200)

    @patch('users.views.requests')
    def test_null_header_request_keyerror(self, mocked_requests):
        response = client.get("/users/login/")
        self.assertEqual(response.status_code, 400)