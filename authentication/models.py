from django.db import models

# Create your models here.
class Users(models.Model):
    fullName = models.CharField(max_length=50)
    login = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField
    password = models.CharField(max_length=20)
    
    # def __str__(self):
    #     return self.login