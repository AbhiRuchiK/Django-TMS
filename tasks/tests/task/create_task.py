from tasks.models import TaskCreateModel


class TaskObject:
    @classmethod
    def create_task_object(cls):
        TaskCreateModel.objects.create(
            task_title="Unit Test",
            task_description="Test models, views, forms and urls",
        )
        return TaskCreateModel.objects.get(id=1)
