from django.contrib import admin

# Register your models here.
from backend.models import User
from .models import User

admin.site.register([User])