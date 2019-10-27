from django.db import models

class Acc(models.Model):
 username=models.CharField(max_length=50)
 area=models.CharField(max_length=50,blank=True)
 acc=models.CharField(max_length=50,blank=True)
 ifsc=models.CharField(max_length=50,blank=True)
 bname=models.CharField(max_length=100,blank=True)
 pin=models.IntegerField(default=835215)
 isgov=models.BooleanField(default=False)
 def __str__(self):
     return self.username
