from django import forms

from django.forms import ModelForm
from .models import ToDoCreate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TodoCreationForm(ModelForm):
    class Meta:
        model=ToDoCreate
        fields="__all__"
        widgets={
            "task_name":forms.TextInput(attrs={"class":"form-control"}),
            "completed": forms.Select(attrs={"class": "form-select"}),
            "created_by": forms.TextInput(attrs={"class": "form-control"})
        }




class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"})
        }

class SigninForm(forms.Form):
    username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control"}))


class SearchForm(forms.Form):
    created_by=forms.CharField(max_length=25,widget=forms.TextInput(attrs={"class":"form-control"}))