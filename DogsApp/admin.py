from django.contrib import admin
from django import forms
from DogsApp import models

admin.site.register(models.Adoptado)
admin.site.register(models.Adoptante)
admin.site.register(models.Refugio)
admin.site.register(models.Avatar)

# Register your models here.
