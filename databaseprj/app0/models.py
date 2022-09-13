from django.db import models

# Create your models here.
class Books_model(models.Model):
	Book_Name=models.CharField(max_length=20)
	Author=models.CharField(max_length=30)
	Language=models.CharField(max_length=10)
	Email=models.EmailField()
	Genre=models.CharField(max_length=15)
	Sales=models.IntegerField()