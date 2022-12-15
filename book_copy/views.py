from os import name
import re
from django import http
from django.shortcuts import render, HttpResponse
from book_copy.models import Book
from Book.models import Post
from .form import DocumentForm
from django.core.files.storage import default_storage
from .models import Profilepic

# Create your views here.


def profile(request):
    posts = list(Post.objects.filter(Uploader=request.user))
    c = len(posts)
    posts = [posts[i:i+3] for i in range(0, len(posts), 3)]
    pic = list(Profilepic.objects.filter(userp=request.user))
    
    context = {
        'posts': posts , 'size' : c , 'pic' : pic[0]
    }
    

    if request.method == "POST":
        abouty = request.POST.get('About',';)')
        imgfile = request.FILES['image']
        obj = Profilepic(userp = request.user ,Image = imgfile,about=abouty)
        Profilepic.objects.filter(userp=request.user).delete()
        obj.save()

    return render(request, 'profile.html',context)


def form(request):
    print("kk")
    
    context = {'Success': False}
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        title = request.POST['title']
        author = request.POST['Author']
        genre = request.POST['Genre']
        desc = request.POST['desc']
        docfile = request.FILES['file']
        imgfile = request.FILES['image']
        price = request.POST['Price']
        bform = Post(Book_name=title, Author=author,
                     Genre=genre, Info=desc, File=docfile, Image=imgfile, Price=price, Uploader=request.user)
        bform.save()
        print(title, desc, author, genre, desc)
        context = {'Success': True}

    
    return render(request, 'form.html', context)


def uploads(request):
    allBooks = Book.objects.all()
    context = {'Books': allBooks}
    # for con in allBooks:
    # print(con.Title)
    return render(request, 'uploads.html', context)
