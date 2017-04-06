from django.views import generic as generic_views

from tunobase.core import utils as core_utils, models as core_models

from app.workspaces import models

class Workspaces(generic_views.ListView):

    def get_queryset(self):
        return models.Workspaces.objects.permitted()

class WorkspaceDetail(generic_views.DetailView):

    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            models.Workspaces,
            slug=self.kwargs['slug']
        )
