from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.CharField(max_length=100)
  email= models.EmailField(null=True)
  age = models.IntegerField()
  roll_no = models.IntegerField(null=True)
  profile_pic = models.ImageField(upload_to='students/', null=True, blank=True)  
  def __str__(self):
   return self.name