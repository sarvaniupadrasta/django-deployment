from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=264)
    lastname = models.CharField(max_length=264)
    email = models.CharField(max_length=264,unique=True)
    
