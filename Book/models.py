from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    Book_name = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    date_uploaded = models.DateTimeField(default=timezone.now)
    Info = models.CharField(max_length=1000)
    Genre = models.CharField(max_length=30)
    Price = models.IntegerField(default=0)
    Uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    Image = models.ImageField(default='default.jpg', upload_to='media/images')
    File = models.FileField(default='default.pdf', upload_to='media/files')
    upvotes = models.ManyToManyField(User, related_name='upv')
    devotes = models.ManyToManyField(User, related_name='dev')
    downloads = models.ManyToManyField(User, related_name='down')
    reads = models.ManyToManyField(User, related_name='reads')
    buy = models.ManyToManyField(User, related_name='buy')


class Saved(models.Model):
    saved = models.ManyToManyField(User, related_name='saved')
    Books = models.ForeignKey(
        Post, related_name='books', on_delete=models.CASCADE)


