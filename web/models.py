#from __future__ import unicode_literals
#import datetime
from django.db import models
from django.contrib.auth.models import User

# Create models here
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __unicode__(self):
        return (self.date , self.amount)



class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return (self.date , self.amount)