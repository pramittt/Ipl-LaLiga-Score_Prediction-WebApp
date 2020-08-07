from django.db import models

# Create your models here.
class Teams(models.Model):

    team = models.CharField(max_length=30)
    img = models.ImageField(upload_to='pics')

class Team(models.Model):

    group = models.CharField(max_length=30)
    img = models.ImageField(upload_to='pics')