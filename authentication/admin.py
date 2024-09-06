from django.contrib import admin

# Register your models here.
from authentication.models import Users

admin.site.register(Users)