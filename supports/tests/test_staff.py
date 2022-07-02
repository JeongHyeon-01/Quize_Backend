from rest_framework.test             import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.test import Client
from users.models import User
from supports.models import Support


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
        User.objects.create(
                id       = 2,
                is_staff = True,
                uid      = '123123123',
                provider = 'google',
                picture  = 'picture.jpg',
                username = 'test',
                email    = 'test@bbb.com'
            )
        self.support=Support.objects.create(id=1,user_id=1, title="test",description="test")

    def tearDown(self):
        Support.objects.all().delete
        User.objects.all().delete()


    def test_posting_staff_retrive(self):
        token = RefreshToken.for_user(User.objects.get(id =2))
        header = {"HTTP_access": str(token.access_token),'HTTP_refresh' : str(token)}
        response = client.get('/supports/help/1/', **header, content_type='application/json')
        self.assertEqual(response.status_code, 200)
    

    def test_posting_staff_put(self):
        token = RefreshToken.for_user(User.objects.get(id =2))
        header = {"HTTP_access": str(token.access_token),'HTTP_refresh' : str(token)}
        data ={"title":"123","description":"123"}
        response = client.put('/supports/help/1/', data=data,**header, content_type='application/json')
        
        self.assertEqual(response.status_code, 200)

    def test_posting_staff_put(self):
        token = RefreshToken.for_user(User.objects.get(id =2))
        header = {"HTTP_access": str(token.access_token),'HTTP_refresh' : str(token)}
        data ={"confirmation":True}
        response = client.post('/supports/help/1/', data=data,**header, content_type='application/json')
        
        self.assertEqual(response.status_code, 200)

    def test_posting_staff_put(self):
        token = RefreshToken.for_user(User.objects.get(id =2))
        header = {"HTTP_access": str(token.access_token),'HTTP_refresh' : str(token)}
        response = client.delete('/supports/help/1/',**header, content_type='application/json')
        
        self.assertEqual(response.status_code, 204)