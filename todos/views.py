from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm
# Create your views here.

def todolist(request):
    todos = Todo.objects.all()
    print(todos)

    return render(request,"todos/list.html",{"todos":todos})

def todo_delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        print(todo)
        todo.delete()

    except:
        print("刪除錯誤")

    return redirect("todo-list")

def todo_create(request):
    return render(request, "todos/create.html",{"form":TodoForm()})