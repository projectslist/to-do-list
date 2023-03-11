from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import TaskList,  TaskCreate, RegisterPage

class TestUrls(SimpleTestCase):

    def test_task_list_url_is_resolved(self):

        url = reverse('tasks')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TaskList)

    def test_register_page_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RegisterPage)

    def test_task_create_url_is_resolved(self):
        url = reverse('task-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TaskCreate)
