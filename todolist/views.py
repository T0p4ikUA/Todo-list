from django.shortcuts import get_object_or_404, redirect
from django.db.models import Count
from django.views.decorators.http import require_POST
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView,
)
from django.urls import reverse_lazy
from todolist.forms import TaskForm, TagForm
from todolist.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "todolist/home.html"
    context_object_name = "tasks"
    paginate_by = 3


@require_POST
def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todolist:home")


class TagListView(ListView):
    model = Tag
    template_name = "todolist/tag_list.html"
    context_object_name = "tags"
    paginate_by = 5

    def get_queryset(self):
        return Tag.objects.annotate(tasks_count=Count("tasks"))


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_form.html"
    success_url = reverse_lazy("todolist:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_form.html"
    success_url = reverse_lazy("todolist:home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todolist/task_confirm_delete.html"
    success_url = reverse_lazy("todolist:home")


class TaskDetailView(DetailView):
    model = Task
    template_name = "todolist/task_detail.html"


class TagDetailView(DetailView):
    model = Tag
    template_name = "todolist/tag_detail.html"
    context_object_name = "tag"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("tasks")


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todolist/tag_form.html"
    success_url = reverse_lazy("todolist:tags")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todolist/tag_form.html"
    success_url = reverse_lazy("todolist:tags")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todolist/tag_confirm_delete.html"
    success_url = reverse_lazy("todolist:tags")
