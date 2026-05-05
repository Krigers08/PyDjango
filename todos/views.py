from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

# READ — show all todos
@login_required
def todo_list(request):
    todos = Todo.objects.filter(owner=request.user)
    form = TodoForm()
    return render(request, 'todos/list.html', {'todos': todos, 'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('todo-list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo-list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# CREATE — add a new todo
@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = request.user
            todo.save()
    return redirect('todo-list')

# UPDATE — mark as done/undone
@login_required
def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk, owner=request.user)
    todo.done = not todo.done
    todo.save()
    return redirect('todo-list')

# DELETE — remove a todo
@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, owner=request.user)
    todo.delete()
    return redirect('todo-list')