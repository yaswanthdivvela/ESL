from django.db import models
from accounts.models import Acc

class Listing(models.Model):
 accs=models.ForeignKey(Acc,on_delete=models.DO_NOTHING,default=None)
 username=models.CharField(max_length=50)
 item=models.CharField(max_length=50)
 invoice=models.CharField(max_length=50)
 pic=models.ImageField()
 ref=models.CharField(max_length=100,default='-')
 quantity=models.IntegerField()
 status=models.BooleanField(default=False)
 def __str__(self):
     return self.username
