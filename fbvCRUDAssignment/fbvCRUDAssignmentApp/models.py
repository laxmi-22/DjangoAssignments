from django.db import models

# Create your models here.
class Course(models.Model):
    Name=models.CharField(max_length=40)
    Description=models.CharField(max_length=100)
    Instructor=models.CharField(max_length=50)
    Rating=models.IntegerField()

