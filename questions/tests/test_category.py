from django.urls import reverse

from rest_framework.test import APITestCase

from questions.models import DevelopmentGroup, Category
from users.models     import User, UserRank


class CategoryTest(APITestCase):
    def setUp(self):
        self.development_group = DevelopmentGroup.objects.create(name='Backend', image='development.jpg')
        self.category          = Category.objects.create(
                                    development_group = self.development_group,
                                    name              = 'test category',
                                    description       = 'test description',
                                    image             = 'category.jpg'
                                )
        
        self.user = User.objects.create(
                            id       = 1,
                            uid      = '123123123',
                            provider = 'google',
                            picture  = 'picture.jpg',
                            username = 'test',
                            email    = 'test@aaa.com'
                        )
     
        self.user_rank = UserRank.objects.create(user_id=1, correct_answer=9, total_time=9, quiz_passed=1, attempt=1)

    def test_category_list(self):
        response = self.client.get(reverse('category-list', args=(self.development_group.id, )))
        self.assertEqual(response.status_code, 200)