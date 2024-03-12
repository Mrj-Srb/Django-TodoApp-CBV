
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.

class CustomLoginView(LoginView):
    
    template_name = "accounts/login.html"
    next_page = "/"
    fields = ['username','password']

class RegisterView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "accounts/register.html"

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            redirect("/")
        return super().get(request, *args, **kwargs)



