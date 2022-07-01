from django.shortcuts import render, HttpResponse, redirect, reverse
# from django.http.response import JsonResponse
from .models import Todo, Task
from pprint import pprint

my_todo_list = {
    'one': {'name': 'laravel', 'priority': 1, 'is_done': False, 'description': 'laravel is a web framework for PHP'},
    'two': {'name': 'django', 'priority': 2, 'is_done': False, 'description': 'django is a web framework for Python'},
    'three': {'name': 'nodejs', 'priority': 3, 'is_done': False, 'description': 'nodejs is a web framework for JavaScript'},
}

def todo_home(request):
    # pprint(vars(request))
    # return HttpResponse("Todo Home")
    return render(request, 'todo/todo.html', context={'my_todo_list': my_todo_list})

def todo_details(request, **kwargs):
    target_todo_name = kwargs.get('todo_name')
    todo_details = my_todo_list.get(target_todo_name)
    return render(request, 'todo/todo_details.html', context={'my_todo': todo_details})


def todo_edit(request,**kwargs):
    target_todo_name = kwargs.get('todo_name')
    return render(request, 'todo/todo_edit.html', context={'my_todo': target_todo_name})

def todo_update(request,**kwargs):
    task_name=kwargs.get('todo_name')
    my_target_todo = my_todo_list.get(task_name)
    my_target_todo['is_done'] = True
    my_target_todo['name'] = 'updated'
    return redirect(reverse('todo:home'))

def todo_done(request, **kwargs):
    target_todo_name = kwargs.get('todo_name')
    my_todo_list.get(target_todo_name)['is_done'] = True
    return redirect(reverse('todo:home'))

def todo_undone(request, **kwargs):
    target_todo_name = kwargs.get('todo_name')
    my_todo_list.get(target_todo_name)['is_done'] = False
    return redirect(reverse('todo:home'))

def todo_delete(request, **kwargs):
    target_todo_name = kwargs.get('todo_name')
    if my_todo_list.get(target_todo_name)['is_done']:
        my_todo_list.pop(target_todo_name)
        return redirect(reverse('todo:home'))
    else:
        return render(request, 'todo/todo.html', context={'my_todo_list': my_todo_list, 'warning_message': 'You cannot delete a todo that is not done yet.'})