'''
Created on 25 Nov 2013

@author: michael
'''
from django.views import generic as generic_views

from tunobase.core import utils as core_utils
from tunobase.core import models


class Events(generic_views.ListView):

    def get_queryset(self):
        return models.Event.objects.permitted()


class EventDetail(generic_views.DetailView):

    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            models.Event,
            slug=self.kwargs['slug']
        )
