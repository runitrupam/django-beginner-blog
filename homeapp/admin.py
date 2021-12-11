from django.contrib import admin
from django.contrib.admin.decorators import register
from homeapp.models import Contact
# Register your models here.

admin.site.register(Contact)