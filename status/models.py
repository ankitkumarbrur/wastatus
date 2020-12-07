from django.db import models

# Create your models here.

class Status(models.Model):
    online = models.DateTimeField(null=True,default=None,auto_now=False, auto_now_add=False)
    offline = models.DateTimeField(null=True,default=None,auto_now=False, auto_now_add=False)
    duration = models.DurationField(null=True,default=None)