'''
Created on 03 Dec 2013

@author: christina
'''
from django.views import generic as generic_views
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect

from tunobase.core import mixins as core_mixins, utils as core_utils, views as core_views
from tunobase.console import mixins as console_mixins
from app.events import models as events_models
from app.authentication import models as users_models

class AdminMixin(console_mixins.ConsoleUserRequiredMixin, core_mixins.PermissionRequiredMixin):
    raise_exception = False

class ConsoleLanding(AdminMixin, TemplateView):
    permission_required = 'events.add_events'
    template_name='console/console/landing_page.html'

#----------------------------------------------------------------------------
# Console: Users
class UsersCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'users.add_users'
    
    def get_success_url(self):
        return reverse('console_users_detail', args=(self.object.pk,))

class UsersUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'users.change_users'
    
    def get_success_url(self):
        return reverse('console_users_detail', args=(self.object.pk,))

    def get_queryset(self):
        return users_models.EndUser.objects.permitted().all()

class UsersDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'users.change_users'

    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            users_models.EndUser, pk=self.kwargs['pk']
        )

class UsersDelete(AdminMixin, core_views.MarkDeleteView):
    permission_required = 'users.delete_users'
    
    def get_success_url(self):
        return reverse('console_events_list')

    def get_queryset(self):
        return users_models.EndUser.objects.permitted().all()

class UsersList(AdminMixin, generic_views.ListView):
    permission_required = 'users.change_users'
    
    def get_queryset(self):
        return users_models.EndUser.objects.all()
#-----------------------------------------------------------------------------

class EventsCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'events.add_events'
    
    def get_success_url(self):
        return reverse('console_media_events_detail', args=(self.object.pk,))

class EventsUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'events.change_events'
    
    def get_success_url(self):
        return reverse('console_media_events_detail', args=(self.object.pk,))

    def get_queryset(self):
        return events_models.Events.objects.permitted().all()

class EventsDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'events.change_events'

    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            events_models.Events, pk=self.kwargs['pk']
        )

class EventsDelete(AdminMixin, core_views.MarkDeleteView):
    permission_required = 'events.delete_events'
    
    def get_success_url(self):
        return reverse('console_media_events_list')

    def get_queryset(self):
        return events_models.Events.objects.permitted().all()

class EventsList(AdminMixin, generic_views.ListView):
    permission_required = 'events.change_events'
    
    def get_queryset(self):
        return events_models.Events.objects.permitted().all()
    
    
