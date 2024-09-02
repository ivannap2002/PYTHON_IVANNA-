from django.contrib import admin

#registrar your models here.
from django.contrib import admin
from .models import Post

admin.site.registrar(Post)