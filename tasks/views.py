from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import TaskCreateModel
from .forms import TaskCreateForm, TaskCommentForm
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    return render(request, "task_management_system_home.html", {})


@login_required
def create_view(request, *args, **kwargs):
    form = TaskCreateForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        form = TaskCreateForm()  # re render

    context = {"form": form}

    return render(request, "task_create.html", context)


@login_required
def all_tasks_view(request):
    context = {"all_tasks_objects": TaskCreateModel.objects.filter(user=request.user)}

    return render(request, "all_tasks_list.html", context)


@login_required
def task_delete_view(request, id):
    task_object = get_object_or_404(TaskCreateModel, id=id)

    if request.method == "POST":
        task_object.delete()
        return redirect("../../")

    context = {"task_object": task_object}

    return render(request, "task_delete.html", context)


@login_required
def update_view(request, id=None):
    task_object = get_object_or_404(TaskCreateModel, id=id)
    create_form = TaskCreateForm(request.POST or None, instance=task_object)
    comment_form = TaskCommentForm(request.POST or None, instance=task_object)

    if "add_comment" in request.POST:
        if comment_form.is_valid():
            instance = comment_form.save()
            instance.save()
            return HttpResponseRedirect("task_edit")
    elif "edit_task" in request.POST:
        if create_form.is_valid():
            instance = create_form.save()
            instance.save()
            return HttpResponseRedirect("task_edit")

    context = {
        "comment_form": comment_form,
        "create_form": create_form,
        "task_object": task_object,
    }
    return render(request, "task_edit.html", context)


@login_required
def comment_delete_view(request, id):
    task_object = get_object_or_404(TaskCreateModel, id=id)
    if request.method == "POST":
        task_object.comment_on_task = ""
        task_object.save()
        return redirect("task_edit", id=task_object.id)

    context = {"task_object": task_object}
    return render(request, "comment_delete.html", context)
