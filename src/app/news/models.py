'''
Created on 25 Nov 2013

@author: michael
'''
from tunobase.core import models as core_models

class News(core_models.BaseContentModel):
    '''
    News
    '''
    default_image_category = 'news'
    
    class Meta:
        verbose_name_plural = 'news'
