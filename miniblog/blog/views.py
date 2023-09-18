from django.shortcuts import render, HttpResponseRedirect
from .forms import RegistrationForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post


def home(request):
    posts = Post.objects.all() # Take all data from Post model and give this data to post
    return render(request, 'blog/home.html', {'posts':posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'blog/dashboard.html',{'posts' : posts})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! You successfully logged in.')
            form.save()
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form' : form})

def user_login(request):
    # if user already logged in go to else part if not then execute if
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']       # take username from form
                user_password = form.cleaned_data['password']   # take password from form
                user = authenticate(username=user_name, password=user_password) # check authenticated or not
                if user is not None:    # if user exist
                    login(request, user)
                    messages.success(request, 'Logged In Successfully')     # on sucess display this message
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form' : form})
    else:
        return HttpResponseRedirect('/dashboard/')


# Add new post

def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                post = Post(title=title, description=description)
                post.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
# Update post

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html',{'form' : form})
    else:
        return HttpResponseRedirect('/login/')
    
# Delete post

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')