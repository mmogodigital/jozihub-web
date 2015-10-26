from django.views import generic as generic_views

from tunobase.core import utils as core_utils, models as core_models

from app.startups import models

class Startup(generic_views.ListView):
    
    def get_queryset(self):
        return models.StartupCompanies.objects.permitted()
    
class StartupDetail(generic_views.DetailView):
    
    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            models.StartupCompanies, 
            slug=self.kwargs['slug']
        )