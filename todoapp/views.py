from django.shortcuts import render,redirect
from .forms import TodoCreationForm,RegistrationForm,SigninForm,SearchForm
from .models import ToDoCreate
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"user/homepage.html")
def todo_register(request):
    form=RegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,"user/registration.html",context)

def todo_signin(request):
    context={}
    form=SigninForm()
    context["form"]=form
    if request.method=="POST":
        form=SigninForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                context={}
                context["form"]=form
                return render(request,"user/login.html",context)
    return render(request,"user/login.html",context)

def todo_create(request):

    context={}
    form = TodoCreationForm()
    context["form"]=form

    if request.method=="POST":
        form=TodoCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"ToDo Added Successfully!!")
            return redirect("todoadd")
        else:
            messages.error(request,"Failed")
            context["form"]=form
            return render(request, "user/todo_create.html", context)
    return render(request,"user/todo_create.html",context)

def todo_list(request):
        todos=ToDoCreate.objects.all()
        context={}
        context["todos"]=todos
        form = SearchForm()
        context["form"]=form
        if request.method=="POST":
            form=SearchForm(request.POST)
            if form.is_valid():
                created_by=form.cleaned_data["created_by"]
                todo=ToDoCreate.objects.filter(created_by__contains=created_by)
                context["todos"]=todo
                return render(request, "user/todo_list.html", context)
        return render(request,"user/todo_list.html",context)

def todo_detail(request,id):
    todo=ToDoCreate.objects.get(id=id)
    context={}
    context["todo"]=todo
    return render(request,"user/todo_detail.html",context)

def todo_change(request,id):
    todo=ToDoCreate.objects.get(id=id)
    form=TodoCreationForm(instance=todo)
    context={}
    context["form"]=form

    if request.method=="POST":
        form=TodoCreationForm(instance=todo,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("todolist")
    return render(request,"user/todo_change.html",context)

def todo_remove(request,id):
    todo=ToDoCreate.objects.get(id=id)
    todo.delete()
    return redirect("todolist")


def todo_signout(request):
    logout(request)
    return redirect("login")


