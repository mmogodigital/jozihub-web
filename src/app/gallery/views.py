'''
Created on 25 Nov 2013

@author: michael
'''
from django.views import generic as generic_views

from tunobase.core import utils as core_utils, models as core_models

from app.gallery import models

class Galleries(generic_views.ListView):
    
    def get_queryset(self):
        return core_models.Gallery.objects.permitted()
    
class GalleryDetail(generic_views.DetailView):
    
    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            core_models.Gallery, 
            slug=self.kwargs['slug']
        )