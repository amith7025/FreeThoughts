from django.db import models
from datetime import datetime


# Create your models here.


class Blog(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    

