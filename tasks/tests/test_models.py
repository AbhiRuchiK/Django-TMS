from django.test import TestCase
from tasks.models import TaskCreateModel
from tasks.tests.task.create_task import TaskObject
from tasks.tests.task.setup_account import setup_account


class TestTaskCreateModel(TestCase):
    def setUp(self):
        self.task_object: TaskCreateModel = TaskObject.create_task_object()

    def test_model_fields(self):
        setup_account(self)
        self.assertEqual(str(self.task_object.task_title), self.task_object.task_title)

        self.assertEqual(
            str(self.task_object.task_description), self.task_object.task_description
        )
        self.assertEqual(
            str(self.task_object.comment_on_task), self.task_object.comment_on_task
        )

    def test_task_title_max_length(self):
        max_length = self.task_object._meta.get_field("task_title").max_length
        self.assertEqual(max_length, 120)
