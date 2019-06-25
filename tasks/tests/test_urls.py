from django.urls import reverse, resolve
from django.test import TestCase
from django.http import HttpRequest
from tasks.tests.task.create_task import TaskObject
from tasks.models import TaskCreateModel
from tasks.views import (
    create_view,
    home_view,
    update_view,
    task_delete_view,
    all_tasks_view,
    comment_delete_view,
)
from tasks.tests.task.setup_account import setup_account


class TestHomeUrl(TestCase):
    def test_root_url_resolves_to_home_view(self):
        path = resolve("/home/")
        self.assertEqual(path.func, home_view)

    def test_home_view_returns_correct_html(self):
        setup_account(self)
        request = HttpRequest()
        request.user = self.user
        response = home_view(request)
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>Task Management System</title>", html)
        self.assertTrue(html.endswith("</html>"))


class TestCreateViewUrl(TestCase):
    def test_create_view_url(self):
        path = resolve("/create/")
        self.assertEqual(path.func, create_view)


class TestAllTasksViewUrl(TestCase):
    def test_all_tasks_view_url(self):
        path = resolve("/tasks/")
        self.assertEqual(path.func, all_tasks_view)


class TestUpdateViewUrl(TestCase):
    def test_update_view_url(self):
        task_object: TaskCreateModel = TaskObject.create_task_object()

        path = resolve(reverse("task_edit", args=[task_object.id]))
        self.assertEqual(path.func, update_view)


class TestDeleteViewUrl(TestCase):
    def test_task_delete_view_url(self):
        task_object: TaskCreateModel = TaskObject.create_task_object()
        path = reverse("task_delete", args=[task_object.id])
        self.assertEqual(resolve(path).func, task_delete_view)


class TestCommentDeleteViewUrl(TestCase):
    def test_comment_delete_view_url(self):
        task_object: TaskCreateModel = TaskObject.create_task_object()
        path = reverse("comment_delete", args=[task_object.id])
        self.assertEqual(resolve(path).func, comment_delete_view)
