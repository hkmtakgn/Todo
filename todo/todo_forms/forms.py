from django import forms
from todo.models import Task

class TodoForm (forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


        widgets = {
            "task_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Input Task"}),
        }
        
        exclude = ["task_slug"]

