from django.views import generic as generic_views

from tunobase.core import utils as core_utils, models as core_models

from app.services import models

class Services(generic_views.ListView):
    
    def get_queryset(self):
        return models.Services.objects.permitted()
    
class ServiceDetail(generic_views.DetailView):
    
    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            models.Services, 
            slug=self.kwargs['slug']
        )