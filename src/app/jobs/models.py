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
    title = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __unicode__(self):
        return u'%s' % self.title

class JobPost(core_models.ContentModel):
    """
    Store a job listing
    """
    location = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    job_categories = models.ManyToManyField(
            JobCategory,
            blank=True,
            null=True,
    )

