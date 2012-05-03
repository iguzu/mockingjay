from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.views.generic import CreateView
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/about/home')


class LoginView(CreateView):
    form_class = LoginForm
