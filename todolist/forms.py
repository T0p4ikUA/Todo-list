from django import forms
from todolist.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "content": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "enter content..."}
            ),
            "deadline": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "is_done": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-select"}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "enter tag name..."}
            )
        }
