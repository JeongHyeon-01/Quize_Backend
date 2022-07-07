from django.test import Client

from rest_framework.test             import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


client = Client()
class SupportNomallyUser(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
                        id       = 1,
                        uid      = '123123123',
                        provider = 'google',
                        picture  = 'picture.jpg',
                        username = 'test',
                        email    = 'test@aaa.com'
                    )
    
    def tearDown(self):
        User.objects.all().delete()

    def test_nomally_user_get(self):
        token    = RefreshToken.for_user(User.objects.get(id =1))
        header   = {"HTTP_access": str(token.access_token),'HTTP_refresh' : str(token)}
        response = client.get('/supports/help/', **header, content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_nomally_user_post(self):
        token    = RefreshToken.for_user(User.objects.get(id=1))
        header   = {"HTTP_access": str(token.access_token),'HTTP_refresh' : str(token)}
        data     = {"title":"123","description":"123"}
        response = client.post('/supports/help/', data=data ,**header, content_type='application/json')
        self.assertEqual(response.status_code, 201)



        