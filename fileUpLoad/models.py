from django.db import models
from authentication.models import Users

# Create your models here.
class Media(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='media_files')
    media = models.FileField(upload_to='documents/')
    title = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)