"""task_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from tasks.views import (
    create_view,
    home_view,
    task_delete_view,
    all_tasks_view,
    update_view,
    comment_delete_view,
)
from accounts.views import (
    login_view,
    create_account_view,
    logout_view
)

urlpatterns = [
    path("admin/", admin.site.urls),
    url("home/", home_view, name="home"),

    path("create/", create_view, name="create_task"),
    path("tasks/", all_tasks_view, name="all_tasks"),
    url(r"^tasks/(?P<id>\d+)/delete/", task_delete_view, name="task_delete"),
    url(r"^tasks/(?P<id>\d+)/", update_view, name="task_edit"),
    url(r"^(?P<id>\d+)/delete/", comment_delete_view, name="comment_delete"),

    path('', login_view, name="login_account"),
    path('accounts/register/', create_account_view, name="create_account"),
    path('accounts/logout/', logout_view, name="logout_account"),

]
