from django.db import models

# Create your models here.
class Students(models.Model):
    First_name=models.CharField(max_length=25)
    Last_name=models.CharField(max_length=25)
    Email=models.EmailField(max_length=60)
    Gender=models.CharField(max_length=10)
    School = models.CharField(max_length=50)
    Books= models.CharField(max_length=30)
    On_Page=models.IntegerField()
    

class Schools(models.Model):
    School=models.CharField(max_length=50)
    Email=models.EmailField(max_length=60)
    Principal=models.CharField(max_length=50)
    Phone=models.CharField(max_length=20)
    Address=models.TextField()

class Books(models.Model):
    Title=models.CharField(max_length=50)
    Author_Name=models.CharField(max_length=50)
    Published_Date=models.DateField()
    No_of_pages=models.IntegerField()
    



