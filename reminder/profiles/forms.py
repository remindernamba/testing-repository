from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistration(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput())
   class Meta():
       model = Profile
       fields = ('username', 'password', 'first_name', 'last_name')