from django.db import models


# Create your models here.
class Services(models.Model):
    pass

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __unicode__(self):
        return self.title
