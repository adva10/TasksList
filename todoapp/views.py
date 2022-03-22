from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render

from todoapp.models import TodoListItem


def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html', {'all_items':all_todo_items})


def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todolist/')


def deleteTodoView(request, i):
    obj_to_del = TodoListItem.objects.get(id=i)
    obj_to_del.delete()
    return HttpResponseRedirect('/todolist/')
