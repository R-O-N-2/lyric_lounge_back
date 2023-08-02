from django.contrib import admin

# Register your models here.
from .models import User
from .models import Work


admin.site.register(User)