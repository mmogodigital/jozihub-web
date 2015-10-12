from django.views import generic as generic_views

from tunobase.core import utils as core_utils, models as core_models

from app.startups import models

class Startup(generic_views.ListView):
    
    def get_queryset(self):
        return core_models.startup_companies.objects.permitted()
    
class StartupDetail(generic_views.DetailView):
    
    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            core_models.startup_companies, 
            slug=self.kwargs['slug']
        )