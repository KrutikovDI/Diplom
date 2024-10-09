from django.contrib import admin
from fileUpLoad.models import Media

# Register your models here.

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['user', 'media', 'title', 'uploaded_at']
    list_filter = ['user',]