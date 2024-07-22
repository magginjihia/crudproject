from django.db import models


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=30, blank=False, null=False)


# def __str__(self): code for sqli db
#     return self.name


#code for mysql db
class Meta:
    db_table = 'student'
