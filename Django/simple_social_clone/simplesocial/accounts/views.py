from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm # grab the form data in forms.py
    success_url = reverse_lazy('login') # on successfull signup, send user back to login page
    template_name = 'accounts/signup.html'
