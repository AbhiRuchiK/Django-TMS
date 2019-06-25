from django.test import TestCase
from tasks.forms import TaskCreateForm, TaskCommentForm


class TestTaskCreateForm(TestCase):
    # valid form data
    def test_valid_form(self):
        form = TaskCreateForm(
            data={"task_title": "Unit Test", "task_description": "Test Form"}
        )
        self.assertTrue(form.is_valid())

    # invalid form data
    def test_invalid_form(self):
        form = TaskCreateForm(data={"task_title": "", "task_description": "Test Form"})
        self.assertFalse(form.is_valid())


class TestTaskCommentForm(TestCase):
    # Valid comment data
    def test_valid_comment(self):
        comment = TaskCommentForm(data={"comment_on_task": "New comment"})
        self.assertTrue(comment.is_valid())

    # invalid comment data
    def test_invalid_comment(self):
        comment = TaskCommentForm(data={"comment_on_task": None})
        self.assertFalse(comment.is_valid())
