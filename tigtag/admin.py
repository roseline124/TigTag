from django.contrib import admin
from .models import Customer, WaitingList

# Register your models here.
admin.site.register(Customer) 
admin.site.register(WaitingList) 

