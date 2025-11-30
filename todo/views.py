from django.shortcuts import render,redirect,get_object_or_404

from todo.todo_forms.forms import TodoForm
from django.contrib import messages
from todo.models import Task

def todo_home_views (request,task_slug=None,task_id=None,search_slug=None):
	edit_task = None
	if search_slug:
		todo_form = TodoForm ()
		todos = Task.objects.filter (task_name__icontains=request.POST.get('task_search'))
	else:
		todos = Task.objects.all()
	if len(todos) > 0:
		todos=todos.order_by("-pk")
	else:
		todos = None
	if task_id and task_slug:
		edit_task = get_object_or_404 (Task,task_slug=task_slug,id=task_id)
		todo_form = TodoForm (instance=edit_task)
	if request.method == "POST":
		todo_form = TodoForm (request.POST,instance=edit_task)
		if todo_form.is_valid():
			todo_form.save(commit=False)
			is_exists = Task.objects.filter(task_name=todo_form.cleaned_data.get('task_name')).exists()
			if is_exists:
				messages.warning(request,'Already exists!')
			else:
				todo_form.save()
				messages.success (request,"Success!")
			return redirect ("todo_home")
	else:
		if task_slug == None and task_id == None:
			todo_form = TodoForm()
	context = dict(
		todo_form=todo_form,
		todos=todos,
	)
	return render (request,"todo_pages/todo-home.html",context)


def todo_del_views (request,task_slug,task_id):
	task = get_object_or_404 (Task,task_slug=task_slug,id=task_id)
	task.delete()
	return redirect ('todo_home')

