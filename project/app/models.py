from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length = 50)
    Email = models.EmailField()
    Password = models.CharField(max_length=30)
    Contact = models.BigIntegerField()
    Qualification= models.CharField(max_length=50)
    Gender =models.CharField(max_length=20)
    State = models.CharField(max_length=20)

