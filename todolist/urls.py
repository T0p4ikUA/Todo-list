from django.urls import path
from todolist.views import (
    home,
    TagListView,
    CreateTodolist,
    UpdateTodolist,
    DeleteTodolist,
    DetailTodolist,
    TagDetailView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    toggle_task_status,
)

app_name = "todolist"

urlpatterns = [
    path("", home, name="home"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("task/add/", CreateTodolist.as_view(), name="create_todolist"),
    path("task/<int:pk>/", DetailTodolist.as_view(), name="detail_todolist"),
    path("task/update/<int:pk>/", UpdateTodolist.as_view(), name="update_todolist"),
    path("task/delete/<int:pk>/", DeleteTodolist.as_view(), name="delete_todolist"),
    path("tag/<int:pk>/", TagDetailView.as_view(), name="tag"),
    path("tag/add/", TagCreateView.as_view(), name="tag_create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
    path("task/toggle/<int:pk>/", toggle_task_status, name="toggle_task_status"),
]
