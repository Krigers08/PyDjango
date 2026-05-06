from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


@login_required
def todo_list(request):
    show_completed = request.GET.get('show_completed', 'false') == 'true'
    search_query = request.GET.get('q', '')
    todos = Todo.objects.filter(owner=request.user)
    if not show_completed:
        todos = todos.filter(done=False)
    if search_query:
        todos = todos.filter(title__icontains=search_query)
    todos = todos.order_by('-priority', 'pk')
    form = TodoForm()
    return render(request, 'todos/list.html', {'todos': todos, 'form': form, 'show_completed': show_completed, 'search_query': search_query})


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


@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = request.user
            todo.save()
    return redirect('todo-list')


@login_required
def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk, owner=request.user)
    todo.done = not todo.done
    todo.save()
    return redirect('todo-list')


@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, owner=request.user)
    todo.delete()
    return redirect('todo-list')


@login_required
def todo_bulk_update(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        selected_ids = request.POST.getlist('selected_todos')
        if selected_ids:
            todos = Todo.objects.filter(pk__in=selected_ids, owner=request.user)
            if action == 'mark_done':
                todos.update(done=True)
            elif action == 'mark_undone':
                todos.update(done=False)
            elif action == 'delete':
                todos.delete()
    return redirect('todo-list')