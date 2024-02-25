from django.db import models
from accounts.models import Customer
# Create your models here.
class payment(models.Model):
    pay=models.IntegerField()
    done=models.BooleanField(editable=False,default=False)
    term=models.IntegerField(default=0)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)