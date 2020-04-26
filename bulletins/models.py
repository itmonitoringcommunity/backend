from django.db import models
from django.utils import timezone


class Bulletin(models.Model):
    id = models.AutoField(primary_key=True)
    smtp = models.CharField(null=False,max_length=250)
    port = models.CharField(null=False,max_length=250)
    username = models.CharField(null=False,max_length=250)
    password = models.CharField(null=False,max_length=250)
    tolist = models.CharField(null=True,blank=True,max_length=250)
    cclist = models.CharField(null=True,blank=True,max_length=250)
    bcclist = models.CharField(null=True,blank=True,max_length=250)

    btype = models.CharField(null=True,max_length=250)
    priority = models.CharField(null=True,max_length=250)
    state = models.CharField(null=True,max_length=250)
    color = models.CharField(default='#000000',max_length=250)

    created_by = models.CharField(null=True,max_length=250)
    code = models.CharField(null=True,max_length=250)
    title = models.CharField(null=True,max_length=250)
    detail = models.TextField(null=True)
    effect = models.TextField(null=True)
    contact = models.TextField(null=True)
    
    begin_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True,blank=True,default=timezone.now)
    duration = models.IntegerField(default='0')

    ticket_case_url = models.CharField(default='#',blank=True,max_length=250)
    ticket_case_id = models.CharField(null=True,blank=True,max_length=250)

    resolved_time = models.DateTimeField(null=True,blank=True,default=timezone.now)
    is_resolved = models.CharField(default='0',max_length=1)
    resolved_by = models.CharField(null=True,blank=True,max_length=250)
    temporary_solution = models.TextField(null=True,blank=True)
    permanent_solution = models.TextField(null=True,blank=True)
    root_cause = models.TextField(null=True,blank=True)
    
    insert_time = models.DateTimeField(null=True,default=timezone.now)
    modify_time = models.DateTimeField(null=True,default=timezone.now)
    is_automated = models.CharField(default='0',max_length=1)
    is_deleted = models.CharField(default='0',max_length=1)
    
    def __str__(self):
        return (self.code + ' - ' + self.title)
