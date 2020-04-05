from django.db import models


class State(models.Model):
    name = models.CharField(null=True,max_length=250)
    description = models.TextField(blank=True)
    color = models.TextField(default='#000000')
    is_deleted = models.CharField(default='0',max_length=1)

    def __str__(self):
        return self.name
