from django.contrib import admin
from .models import Post, Saved
from django.contrib.auth.models import User
admin.site.register(Post)
admin.site.register(Saved)
# Register your models here.