from django.contrib import admin
from .models import Category, Item  # .models because in the same directory


# Register your models here.  # to register the model write this admin.site.register("MODEL NAME")
admin.site.register(Category)
admin.site.register(Item)

