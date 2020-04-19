from django.db import models


class Mail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True,max_length=250)
    description = models.TextField(blank=True)

    smtp = models.CharField(null=False,max_length=250)
    port = models.CharField(null=False,max_length=250)
    username = models.CharField(null=False,max_length=250)
    password = models.CharField(null=False,max_length=250)
    tolist = models.CharField(null=True,blank=True,max_length=250)
    cclist = models.CharField(null=True,blank=True,max_length=250)
    bcclist = models.CharField(null=True,blank=True,max_length=250)

    is_deleted = models.CharField(default='0',max_length=1)

    def __str__(self):
        return self.name
