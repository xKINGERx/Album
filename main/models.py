from django.db import models

# Create your models here.

class banner(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Date = models.DateTimeField('date published')
    Summary = models.TextField(max_length=30)