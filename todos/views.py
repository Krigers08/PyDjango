from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

# READ — show all todos
def todo_list(request):
    todos = Todo.objects.all()
    form = TodoForm()
    return render(request, 'todos/list.html', {'todos': todos, 'form': form})

# CREATE — add a new todo
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('todo-list')

# UPDATE — mark as done/undone
def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.done = not todo.done
    todo.save()
    return redirect('todo-list')

# DELETE — remove a todo
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo-list')