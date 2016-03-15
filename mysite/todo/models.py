from __future__ import unicode_literals

from django.db import models

import datetime 
PRIORITY_CHOICES = ( 

  (1, 'Low'), 

  (2, 'Normal'), 

  (3, 'High'), 

) 

# Create your models here.

class List(models.Model): 
  title = models.CharField(max_length=256,unique=True)

class Item(models.Model): 
  title = models.CharField(max_length=256) 
  created_date = models.DateTimeField(default=datetime.datetime.now) 
  priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
  completed = models.BooleanField(default=False) 
  todo_list = models.ForeignKey(List)