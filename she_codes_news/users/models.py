from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    name = models.CharField (max_length=200, blank=true)
    bio =
    email = 
    profile_picture = 
    linkedin = 
    instagram = 
    github = 
    def __str__(self):
        return self.username


