from django.contrib import admin
from .models import Item,Expenditure,Bank

# Register your models here.
admin.site.register(Item)
admin.site.register(Expenditure)
admin.site.register(Bank)