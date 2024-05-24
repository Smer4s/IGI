from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import (Category, About,
Question,Article, Contact, Cart,
Employee, Discount, Review, Client, Sale, 
Service, Schedule, Room, PlannedVisit)

# Register your models here.
admin.site.register(
    [Category,About,Question, 
    Article, Contact, Employee, 
    Discount, Review, Client,
    Sale, Schedule, Service, Room,
    Cart, PlannedVisit, Permission])
