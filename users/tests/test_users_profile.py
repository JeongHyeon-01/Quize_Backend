from django.test import Client

from rest_framework.test             import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models  import *


client = Client()

class UserProfileTest(APITestCase):
    def setUp(self):
        user = User.objects.create(
            id       = "1",
            uid      = '123123123',
            username = "test",
            email    = "test@gmail.com",
            picture  = "https://ifh.123123/g/ElNIU1.jpg",
        )
        UserRank.objects.create(user_id=user.id)

    def tearDown(self):
        User.objects.all().delete()

    def test_user_profile_success(self):
        token    = RefreshToken.for_user(User.objects.get(id =1))
        header   = {"HTTP_access": str(token.access_token),'HTTP_refresh' : str(token)}
        response = client.get('/users/profile/', **header, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            [
                {
                    'id'        : 1,
                    'uid'       : '123123123',
                    'username'  : 'test',
                    'email'     : 'test@gmail.com',
                    'picture'   : 'https://ifh.123123/g/ElNIU1.jpg',
                    'last_login': None,
                    'rank_set'  : [{'correct_answer': 0, 'total_time': 0, 'quiz_passed': 0, 'attempt': 0}]
                }
            ]
        )