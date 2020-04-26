from django.db import models
from django.utils import timezone

class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True,max_length=250)
    description = models.TextField(blank=True)
    path = models.CharField(null=True,blank=True,max_length=250)
    delay = models.IntegerField(default=10)    
    output = models.TextField(blank=True)
    result = models.CharField(default='0',max_length=1)

    start_time = models.DateTimeField(null=True,blank=True,default=timezone.now)
    is_scheduled = models.CharField(default='0',max_length=1)
    is_deleted = models.CharField(default='0',max_length=1)

    def __str__(self):
        return self.name
