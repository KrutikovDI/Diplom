from django.contrib import admin
from authentication.models import Users

# Register your models here.


# admin.site.register(Users)

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'login', 'email', 'password', 'admin',]
    list_filter = ['admin',]