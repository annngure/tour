from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    name= models.CharField(max_length=100,null=True)
    occupation= models.CharField(max_length=100,null=True)
    profile_image = models.ImageField(upload_to = 'image/')
    Location = models.CharField(max_length=255, null=True)
    email=models.EmailField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.name
    

class Locals(models.Model):
    name= models.CharField(max_length=100,null=True)
    Location = models.CharField(max_length=255, null=True)
    email=models.EmailField()
    phonenumber=models.IntegerField(max_length=255, null=True)

    def save_locals(self):
        self.save()

    def delete_locals(self):
        self.delete()
    
    def __str__(self):
        return self.name