from django.db import models
from django.conf import settings


class TaskCreateModel(models.Model):
    task_title = models.CharField(max_length=120)
    task_description = models.TextField(blank=True, null=True)
    comment_on_task = models.TextField(
        max_length=1000, default="", blank=True, editable=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.task_title}, {self.task_description}, {self.comment_on_task}"
