from django.db import models
from django.utils import timezone
# Create your models here.

class WebUser(models.Model):
    ip = models.GenericIPAddressField()
    pv = models.IntegerField(default=1)
    create_time = models.DateTimeField(default=timezone.now())
    update_time = models.DateTimeField(blank=True,null=True)

    def __unicode__(self):
        return "{0} {1}".format(self.ip,self.pv)