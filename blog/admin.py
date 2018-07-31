from django.contrib import admin

# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import User
from .models import Request

admin.site.register(User)
admin.site.register(Request)