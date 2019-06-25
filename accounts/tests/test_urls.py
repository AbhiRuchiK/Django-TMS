from django.urls import resolve, reverse
from tests import TestCase
from accounts.views import login_view, create_account_view, logout_view


class TestLoginUrl(TestCase):
    def test_login_view_url(self):
        path = resolve(reverse("login_account"))
        self.assertEqual(path.func, login_view)


class TestCreateAccountUrl(TestCase):
    def test_create_account_view_url(self):
        path = resolve(reverse("create_account"))
        self.assertEqual(path.func, create_account_view)


class TestLogoutUrl(TestCase):
    def test_logout_view_url(self):
        path = resolve(reverse("logout_account"))
        self.assertEqual(path.func, logout_view)
