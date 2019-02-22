from django.db import models

class Events(models.Model):
    pass
    class Meta:
        verbose_name = 'Events'
        verbose_name_plural = 'Events'

    def __unicode__(self):
        return self.title
