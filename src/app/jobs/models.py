'''
Created on 25 Nov 2013

@author: michael
'''
from django.db import models

from tunobase.core import models as core_models

class JobCategory(models.Model):
    """
    List various job cateorgies
    """
    title = models.CharField(max_length=255, required=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return u'%s' % self.title

class JobPost(core_models.models.ContentModel):
    """
    Store a job listing
    """
    job_categories = models.ManyToManyField(
            JobCategory,
            blank=True,
            null=True,
    )

