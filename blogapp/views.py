from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import BlogArticle
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    blogs = BlogArticle.objects.all()
    if request.method=="POST":
        usernames=request.POST['username']
        passwords=request.POST['password']
        user = authenticate(username=usernames,password=passwords)
        if user is not None:
            login(request,user)
            return render(request,'blogapp/main.html',{'testvar':'Test string 2','blogs':blogs,'user':user})

    return render(request,'blogapp/main.html',{'testvar':'Test string 2','blogs':blogs,'user':None})
def createBlog(request):
    blogs=BlogArticle.objects.all()
    newBlog=BlogArticle()
    newBlog.title=request.POST['title']
    newBlog.blog_content=request.POST['blog_content']
    newBlog.author=request.user
    newBlog.save()
    return render(request,'blogapp/main.html',{'testvar':'Test string 2','blogs':blogs,'user':request.user})