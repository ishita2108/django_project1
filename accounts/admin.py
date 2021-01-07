from django.contrib import admin

# Register your models here.

from .models import *               #showing the model 'Customer' in admin panel

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)