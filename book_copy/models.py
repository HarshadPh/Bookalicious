from django.db import models
import os
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    btitle = models.TextField(max_length=30)
    bauthor = models.TextField(max_length=30)
    bgenre = models.TextField(max_length=30)
    bpreface = models.TextField()
    bfile = models.FileField(default='download.jpg', upload_to='static/')

    def __str__(self):
        return self.btitle


class Profilepic(models.Model):
    userp = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.TextField(default=" ",max_length=50)
    Image = models.ImageField(default='default.jpg', upload_to='media/images')

    def __str__(self):
        return self.userp.username
