from django.db import models


class BType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, max_length=250)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_deleted = models.CharField(default='0',max_length=1)

    def __str__(self):
        return self.name
