from django.contrib import admin
from django import forms
from DogsApp import models
from .models import BlogPost

admin.site.register(models.Adoptado)
admin.site.register(models.Refugio)
admin.site.register(models.Avatar)
admin.site.register(BlogPost)

# admin.site.register(models.Adoptante)

# Register your models here.
