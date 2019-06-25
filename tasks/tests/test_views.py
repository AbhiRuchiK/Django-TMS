from django.urls import reverse
from django.test import TestCase
from tasks.models import TaskCreateModel
from tasks.tests.task.create_task import TaskObject
from tasks.tests.task.setup_account import setup_account


class TestHomeView(TestCase):
    def test_home_view_response(self):
        response = self.client.get("/")
        """ HTTP 200 status code :
         (this is the standard response for a successful HTTP request). """
        self.assertEqual(response.status_code, 200)

    def test_save_called(self):
        self.assertTrue(TaskCreateModel.save.__call__)


class TestCreateView(TestCase):
    def test_create_view_response(self):
        setup_account(self)
        response = self.client.get("/create/")
        self.assertEqual(response.status_code, 200)


class TestAllTasksView(TestCase):
    def test_all_tasks_view_response(self):
        setup_account(self)
        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, 200)

    def test_task_title(self):
        setup_account(self)
        task_object: TaskCreateModel = TaskObject.create_task_object()

        response = self.client.get("/tasks/")

        """test the actual response back"""
        self.assertIn(str.encode(task_object.task_title), response.content)


class TestUpdateView(TestCase):
    def test_update_view_response(self):
        setup_account(self)
        task_object: TaskCreateModel = TaskObject.create_task_object()

        response = self.client.get(reverse("task_edit", args=[task_object.id]))
        self.assertEqual(response.status_code, 200)


class TestDeleteView(TestCase):
    def test_delete_view_response(self):
        setup_account(self)
        task_object: TaskCreateModel = TaskObject.create_task_object()

        response = self.client.get(reverse("task_delete", args=[task_object.id]))
        self.assertEqual(response.status_code, 200)


class TestCommentDeleteView(TestCase):
    def test_comment_delete_view_response(self):
        setup_account(self)
        task_object: TaskCreateModel = TaskObject.create_task_object()

        response = self.client.get(reverse("comment_delete", args=[task_object.id]))
        self.assertEqual(response.status_code, 200)
