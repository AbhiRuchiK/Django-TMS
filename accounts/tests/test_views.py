from tests import TestCase
from tasks.tests.task.setup_account import setup_account


class TestLoginView(TestCase):
    def test_login_view_response(self):
        setup_account(self)
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)


class TestCreateAccountView(TestCase):
    def test_create_account_view_response(self):
        setup_account(self)
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)


class TestLogoutView(TestCase):
    def test_logout_view_response(self):
        setup_account(self)
        response = self.client.get("/accounts/logout/", follow=True)
        self.assertEqual(response.status_code, 200)
