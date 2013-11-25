'''
Created on 25 Nov 2013

@author: michael
'''
from django.views import generic as generic_views

from tunobase.core import utils as core_utils

from app.news import models

class News(generic_views.ListView):
    
    def get_queryset(self):
        return models.News.objects.permitted()
    
class NewsDetail(generic_views.DetailView):
    
    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            models.News, 
            slug=self.kwargs['slug']
        )