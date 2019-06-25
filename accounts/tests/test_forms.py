from django.contrib.auth.models import User
from django.test import TestCase


class TestUserLoginForm(TestCase):
    def test_valid_login_form(self):
        self.user = User.objects.create_user(
            username="testuser", email="tms@gmail.com", password="tms@1234"
        )
        login = self.client.login(username="testuser", password="tms@1234")
        self.assertTrue(login)

    def test_invalid_login_form(self):
        self.user = User.objects.create_user(
            username="testuser", email="tms@gmail.com", password="tms@1234"
        )
        login = self.client.login(username="test", password="tms@1234")
        self.assertFalse(login)


class TestUserCreateForm(TestCase):
    def test_valid_create_form(self):
        self.user = User.objects.create_user(
            username="testuser", email="tms@gmail.com", password="tms@1234"
        )
        self.assertTrue(self.user)

    def test_invalid_create_form(self):
        self.user = User.objects.create_user(username="testuser")
        self.assertFalse(self.user.save())
