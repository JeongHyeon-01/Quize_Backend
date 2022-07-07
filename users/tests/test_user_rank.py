from django.urls import reverse

from rest_framework.test             import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User, UserRank


class TestUserRank(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
                            id       = 1,
                            uid      = '123123123',
                            provider = 'google',
                            picture  = 'picture.jpg',
                            username = 'test',
                            email    = 'test@aaa.com'
                        )
     
        self.user_rank = UserRank.objects.create(
                                    user_id        = 1,
                                    correct_answer = 9,
                                    total_time     = 9,
                                    quiz_passed    = 1,
                                    attempt        = 1
                                )

    def test_user_rank_create(self):
        refresh = RefreshToken.for_user(self.user)
        header = {'HTTP_access': str(refresh.access_token),'HTTP_refresh' : str(refresh)}  

        data = {
            "correct_answer": 8,
            "total_time"    : 9,
            "quiz_passed"   : 1,
            "attempt"       : 1
        }

        response = self.client.post(reverse('user-rank'), data, **header)
        self.assertEqual(response.status_code, 201)

    def test_user_rank_get(self):
        refresh  = RefreshToken.for_user(self.user)
        header   = {'HTTP_access': str(refresh.access_token), 'HTTP_refresh':str(refresh)}

        response = self.client.get(reverse('user-rank'), **header)
        self.assertEqual(response.status_code, 200)