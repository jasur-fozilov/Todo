from django.shortcuts import redirect, render
from .models import TodoList
# Create your views here.
def AllTodoItems(request):
    all_objects=TodoList.objects.all()
    return render(request,'todo/index.html',{'all_objects':all_objects})
    
def AddTodoItem(request):
    x=request.POST['content']
    new_item=TodoList(content=x)
    new_item.save()
    return redirect('AllTodoItems')

def DeleteTodoItem(request,pk):
    d=TodoList.objects.get(pk=pk)
    d.delete()
    return redirect('AllTodoItems')
def updateItem(request,pk):
    item=TodoList.objects.get(pk=pk)
    return render(request,'todo/update.html',{'item':item})

def UpdateTodoItem(request,pk):
    object=request.POST['update']
    u=TodoList.objects.get(pk=pk)
    u.content=object
    u.save()
    return redirect('AllTodoItems')