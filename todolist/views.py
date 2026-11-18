from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Count
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


def home(request):
    task_list = Task.objects.prefetch_related("tags").all()
    paginator = Paginator(task_list, 3)
    page_number = request.GET.get("page")
    tasks = paginator.get_page(page_number)
    content = {
        "tasks": tasks,
    }
    return render(request, "todolist/home.html", content)


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


class CreateTodolist(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_form.html"
    success_url = reverse_lazy("todolist:home")


class UpdateTodolist(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_form.html"
    success_url = reverse_lazy("todolist:home")


class DeleteTodolist(DeleteView):
    model = Task
    template_name = "todolist/task_confirm_delete.html"
    success_url = reverse_lazy("todolist:home")


class DetailTodolist(DetailView):
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
