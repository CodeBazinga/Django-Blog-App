from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class BlogForm(forms.ModelForm): 
    class Meta:  
        model = BlogModel 
        fields = [ "title", "description","image"] 


# class CreateUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password1', 'password2']        
