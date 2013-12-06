'''
Created on 25 Nov 2013

@author: michael
'''
from django.db import models
from django.contrib.sites.models import Site

from tunobase.core import models as core_models

class JHGalleryImage(core_models.ImageModel, core_models.StateModel):
    '''
    A model to store Gallery Images
    '''
    order = models.PositiveIntegerField(default=0, db_index=True)
    sites = models.ManyToManyField(Site, blank=True, null=True)
    
    class Meta:
        ordering = ['order', '-publish_at']
    
    def __unicode__(self):
        return u'%s %s' % (self.image, self.sites.all())
    
    @property
    def gallery(self):
        try:
            return self.galleries.all()[0]
        except IndexError:
            return None

class JHGallery(core_models.BaseContentModel):
    '''
    Containing model for Gallery Images
    '''
    images = models.ManyToManyField(
        JHGalleryImage, 
        related_name='galleries', 
        blank=True, 
        null=True
    )
    
    default_image_category = 'gallery'
    
    class Meta:
        verbose_name_plural = 'galleries'
    
    def __unicode__(self):
        return u'%s' % self.title
