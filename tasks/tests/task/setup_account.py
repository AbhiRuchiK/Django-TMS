from django.contrib.auth.models import User


def setup_account(self):
    self.user = User.objects.create_user(
        username="testuser", email="tms@gmail.com", password="tms@1234"
    )
    self.client.login(username="testuser", password="tms@1234")
