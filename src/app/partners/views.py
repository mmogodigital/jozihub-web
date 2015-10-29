'''
Created on 25 Nov 2013

@author: michael
'''
from django.views import generic as generic_views

from app.partners import models

class Partners(generic_views.ListView):
    
    def get_queryset(self):
        return models.Partner.objects.permitted()
