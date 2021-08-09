from django.urls import path
from todoapp import views

urlpatterns=[
    path('home',views.index,name="home"),
    path('accounts/register', views.todo_register, name="register"),
    path('accounts/signin', views.todo_signin, name="login"),
    path('todos/add',views.todo_create,name="todoadd"),
    path('todos', views.todo_list, name="todolist"),
    path('todos/<int:id>', views.todo_detail, name="tododetail"),
    path('todos/change/<int:id>',views.todo_change, name="todochange"),
    path('todos/remove/<int:id>', views.todo_remove, name="todoremove"),
    path('accounts/signout', views.todo_signin, name="logout"),

]