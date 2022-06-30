from django.urls import reverse

from rest_framework.test import APITestCase

from questions.models import DevelopmentGroup, Category, Question, Answer
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


class QuizTest(APITestCase):
    def setUp(self):
        self.development_group = DevelopmentGroup.objects.create(name='Backend', image='development.jpg')
        self.category          = Category.objects.create(
                                    id                = 1,
                                    development_group = self.development_group,
                                    name              = 'test category',
                                    description       = 'test description',
                                    image             = 'category.jpg'
                                )
                                
        Question.objects.bulk_create([
            Question(id=1, category_id=1, content='aaa', image='aaa.jpg'),
            Question(id=2, category_id=1, content='bbb', image='bbb.jpg'),
            Question(id=3, category_id=1, content='ccc', image='ccc.jpg'),
            Question(id=4, category_id=1, content='ddd', image='ddd.jpg'),
            Question(id=5, category_id=1, content='eee', image='eee.jpg'),
            Question(id=6, category_id=1, content='fff', image='fff.jpg'),
            Question(id=7, category_id=1, content='ggg', image='ggg.jpg'),
            Question(id=8, category_id=1, content='hhh', image='hhh.jpg'),
            Question(id=9, category_id=1, content='iii', image='iii.jpg'),
            Question(id=10, category_id=1, content='jjj', image='jjj.jpg')
        ])

        Answer.objects.bulk_create([
            Answer(id=1, question_id=1, content='aaaa', image='aaaa.jpg'),
            Answer(id=2, question_id=1, content='bbbb', image='bbbb.jpg'),
            Answer(id=3, question_id=1, content='cccc', image='cccc.jpg'),
            Answer(id=4, question_id=1, content='dddd', image='dddd.jpg'),
            Answer(id=5, question_id=1, content='eeee', image='eeee.jpg'),
            Answer(id=6, question_id=2, content='ffff', image='ffff.jpg'),
            Answer(id=7, question_id=2, content='gggg', image='gggg.jpg'),
            Answer(id=8, question_id=2, content='hhhh', image='hhhh.jpg'),
            Answer(id=9, question_id=2, content='iiii', image='iiii.jpg'),
            Answer(id=10, question_id=2, content='jjjj', image='jjjj.jpg'),
            
            Answer(id=11, question_id=3, content='kkkk', image='kkkk.jpg'),
            Answer(id=12, question_id=3, content='llll', image='llll.jpg'),
            Answer(id=13, question_id=3, content='mmmm', image='mmmm.jpg'),
            Answer(id=14, question_id=3, content='nnnn', image='nnnn.jpg'),
            Answer(id=15, question_id=3, content='oooo', image='oooo.jpg'),
            Answer(id=16, question_id=4, content='pppp', image='pppp.jpg'),
            Answer(id=17, question_id=4, content='qqqq', image='qqqq.jpg'),
            Answer(id=18, question_id=4, content='rrrr', image='rrrr.jpg'),
            Answer(id=19, question_id=4, content='ssss', image='ssss.jpg'),
            Answer(id=20, question_id=4, content='tttt', image='tttt.jpg'),

            Answer(id=21, question_id=5, content='uuu', image='uuu.jpg'),
            Answer(id=22, question_id=5, content='vvvv', image='vvvv.jpg'),
            Answer(id=23, question_id=5, content='wwww', image='wwww.jpg'),
            Answer(id=24, question_id=5, content='xxxx', image='xxxx.jpg'),
            Answer(id=25, question_id=5, content='yyyy', image='yyyy.jpg'),
            Answer(id=26, question_id=6, content='zzzz', image='zzzz.jpg'),
            Answer(id=27, question_id=6, content='aaaaa', image='aaaaa.jpg'),
            Answer(id=28, question_id=6, content='bbbbb', image='bbbbb.jpg'),
            Answer(id=29, question_id=6, content='ccccc', image='ccccc.jpg'),
            Answer(id=30, question_id=6, content='ddddd', image='ddddd.jpg'),

            Answer(id=31, question_id=7, content='eeeee', image='eeeee.jpg'),
            Answer(id=32, question_id=7, content='fffff', image='fffff.jpg'),
            Answer(id=33, question_id=7, content='ggggg', image='ggggg.jpg'),
            Answer(id=34, question_id=7, content='hhhhh', image='hhhhh.jpg'),
            Answer(id=35, question_id=7, content='iiiii', image='iiiii.jpg'),
            Answer(id=36, question_id=8, content='jjjjj', image='jjjjj.jpg'),
            Answer(id=37, question_id=8, content='kkkkk', image='kkkkk.jpg'),
            Answer(id=38, question_id=8, content='lllll', image='lllll.jpg'),
            Answer(id=39, question_id=8, content='mmmmm', image='mmmmm.jpg'),
            Answer(id=40, question_id=8, content='nnnnn', image='nnnnn.jpg'),

            Answer(id=41, question_id=9, content='ooooo', image='ooooo.jpg'),
            Answer(id=42, question_id=9, content='ppppp', image='ppppp.jpg'),
            Answer(id=43, question_id=9, content='qqqqq', image='qqqqq.jpg'),
            Answer(id=44, question_id=9, content='rrrrr', image='rrrrr.jpg'),
            Answer(id=45, question_id=9, content='sssss', image='sssss.jpg'),
            Answer(id=46, question_id=10, content='ttttt', image='ttttt.jpg'),
            Answer(id=47, question_id=10, content='uuuuu', image='uuuuu.jpg'),
            Answer(id=48, question_id=10, content='vvvvv', image='vvvvv.jpg'),
            Answer(id=49, question_id=10, content='wwwww', image='wwwww.jpg'),
            Answer(id=50, question_id=10, content='xxxxx', image='xxxxx.jpg'),
        ])

    def tearDown(self):
        Question.objects.all().delete()
        Answer.objects.all().delete()

    def test_quiz_main_page(self):
        response = self.client.get(reverse('quiz-main', args=(self.category.id, )))
        self.assertEqual(response.status_code, 200)