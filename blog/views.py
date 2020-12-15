from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *


# def registerPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)

# 				return redirect('login')
			

# 		context = {'form':form}
# 		return render(request, 'blog/register.html', context)


# def loginPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password =request.POST.get('password')

# 			user = authenticate(request, username=username, password=password)

# 			if user is not None:
# 				login(request, user)
# 				return redirect('create')
# 			else:
# 				messages.info(request, 'Username OR password is incorrect')

# 		context = {}
# 		return render(request, 'blog/login.html', context)


# def logoutUser(request):
# 	logout(request)
# 	return redirect('login')



def home(request):
    return render(request,'blog/home.html')


def create(request):
    form = BlogForm()
    if request.method=='POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

    context= {'form' : form}
    return render(request,'blog/create.html',context)
     


def displayBlog(request):
    blog = BlogModel.objects.all()
    context = {'blog':blog}
    return render(request,'blog/display.html',context)       



# @login_required(login_url='login')
def deletelist(request, id): 
    # fetch the object related to passed id 
    blog = get_object_or_404(BlogModel, id = id) 
    if request.method =="POST": 
        # delete object 
        blog.delete() 
        # after deleting redirect to home page 
        return redirect("/") 
    context = {}
    return render(request, "blog/delete.html", context) 

# @login_required(login_url='login')
def updatelist(request, id): 
    # dictionary for initial data with field names as keys 
    # fetch the object related to passed id 
    blog = get_object_or_404(BlogModel, id = id)  
    form = BlogForm(instance = blog)
    if(request.method == 'POST'):
        form = BlogForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            form.save()
        return redirect('/')
    context ={'form':form}
    return render(request,'blog/update.html',context)