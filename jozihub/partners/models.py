from django.db import models


# Create your models here.
class Partners(models.Model):
    pass

    class Meta:
        verbose_name = 'Partners'
        verbose_name_plural = 'Partners'

    def __unicode__(self):
        return self.title
