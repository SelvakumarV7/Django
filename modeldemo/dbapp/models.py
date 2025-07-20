from django.db import models

# Create your models here.

class Employee(models.Model):
    empNo = models.IntegerField()
    empName = models.CharField(max_length=50)
    empSalary = models.IntegerField
    empAddress = models.CharField(max_length=100)