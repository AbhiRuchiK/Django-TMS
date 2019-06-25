from django import forms
from .models import TaskCreateModel


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = TaskCreateModel
        fields = ["task_title", "task_description"]


class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = TaskCreateModel
        widgets = {"comment_on_task": forms.Textarea(attrs={"rows": 2, "cols": 60})}
        fields = ["comment_on_task"]

    def clean(self, *args, **kwargs):
        comment_on_task = self.cleaned_data.get("comment_on_task")

        if comment_on_task is "":
            raise forms.ValidationError("comment is required")

        return super(TaskCommentForm, self).clean(*args, **kwargs)
