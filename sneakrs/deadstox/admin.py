from django.contrib import admin

# Register your models here.
from .models import Closets, Sneakers

admin.site.register(Closets)
admin.site.register(Sneakers)
