from django.db import models


    
class EventUsers(models.Model):
    name = models.CharField(max_length =600,db_index = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length =900,unique = True)
    
    
class Event(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    event_date = models.DateField()
    notification = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length = 1200,db_index = True)
    users = models.ManyToManyField(EventUsers,related_name="userevents")
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length = 5000,null=True,blank=True)
    

