from django.shortcuts import render, redirect

from todoApp.forms import TodoForm
from todoApp.models import Todo


# Create your views here.
def home(request):
    return render(request,'index.html')

def error(request):
    return render(request,'404.html')


# def todoinput(request):
#     return render(request,'todoinput.html')

def addTodo(request):
        form = TodoForm
        if request.method == 'POST':
            form1 = TodoForm(request.POST)
            if form1.is_valid():
                form1.save()
                return redirect('todoview')
        return render(request,'todoadd.html',{"form":form})


def todoView(request):
    data = Todo.objects.all()
    return render(request,'todoview.html',{"data":data})


# delete

def deleteData(request,id):
    data = Todo.objects.get(id=id)
    data.delete()
    return redirect("todoview")


# Update

def updateData(request,id):
    data = Todo.objects.get(id=id)
    form = TodoForm(instance=data)
    if request.method == 'POST':
        form1 = TodoForm(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('todoview')
    return render(request,'update.html',{"form":form})