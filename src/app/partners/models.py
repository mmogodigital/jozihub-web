'''
Created on 25 Nov 2013

@author: michael
'''
from django.db import models

from tunobase.core import models as core_models

class Partner(core_models.ContentModel):
    '''
    Partners
    '''
    external_link = models.URLField(max_length=255)
    
    default_image_category = 'partner'