"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from todo.views import todo_home_views,todo_del_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", todo_home_views, name='todo_home'),
    path("<slug:search_slug>", todo_home_views, name='todo_search'),
    path("/save-todo/", todo_home_views, name="todo_save"),
    path("<slug:task_slug>/<int:task_id>", todo_home_views, name="edit_task"),
    path("<slug:task_slug>/<int:task_id>/del", todo_del_views, name="del_task"),
]

