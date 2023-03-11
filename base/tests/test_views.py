from datetime import  date
from django.test import TestCase
from django.urls import reverse
from base.models import Task
from django.contrib.auth import  get_user_model, authenticate


class TestViews(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()
        self.timestamp = date.today()
        self.task = Task(user=self.user,
                         title = 'title for testing',
                         description='description',
                         complete=False,
                         )
        self.task.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_read_task(self):
        self.assertEqual(self.task.user, self.user)
        self.assertEqual(self.task.title, 'title for testing')
        self.assertEqual(self.task.description, 'description')
        self.assertEqual(self.task.complete, False)


class AllTasksViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test2',
                                                         password='12test12',
                                                         email='test@example.com')
        self.user.save()
        self.timestamp = date.today()
        self.client.login(username='test2', password='12test12')

    def tearDown(self):
        self.user.delete()

    def test_task_list_GET(self):
        response = self.client.get(reverse('tasks'))
        self.assertEquals(response.status_code, 200)

    def test_task_create_POST(self):

        response = self.client.post(reverse('task-create'))
        self.assertEquals(response.status_code,200)



