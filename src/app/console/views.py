'''
Created on 03 Dec 2013

@author: christina
'''
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views import generic as generic_views
from django.views.generic.base import TemplateView

from tunobase.core import (
    mixins as core_mixins, 
    utils as core_utils, 
    views as core_views, 
    constants as core_constants
)
from tunobase.console import mixins as console_mixins
from tunobase.core.models import Gallery

from app.authentication.models import EndUser
from app.console import forms
from app.events.models import Event 
from app.jobs.models import JobPost
from app.news.models import News 


class AdminMixin(
    console_mixins.ConsoleUserRequiredMixin, 
    core_mixins.PermissionRequiredMixin
):
    raise_exception = False

class ConsoleLanding(AdminMixin, TemplateView):
    permission_required = 'events.add_events'

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
        return EndUser.objects.all()


class UsersDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'users.change_users'

    def get_object(self):
        return get_object_or_404(
            EndUser, pk=self.kwargs['pk']
        )


class UsersDelete(AdminMixin, core_views.MarkDeleteView):
    permission_required = 'users.delete_users'

    def get_success_url(self):
        return reverse('console_users_list')

    def get_queryset(self):
        return EndUser.objects.all()


class UsersList(AdminMixin, core_mixins.FilterMixin, generic_views.ListView):
    permission_required = 'users.change_users'

    allowed_filters = {
            'first_name': 'first_name__icontains',
            'last_name': 'last_name__icontains',
            'email': 'email__icontains',
    }

    def get_context_data(self, **kwargs):
        context = super(UsersList, self).get_context_data(**kwargs)
        context['filter_form'] = forms.UserFilter(self.request.GET)
        return context

    def get_queryset(self):
        return EndUser.objects.filter(**self.get_queryset_filters())

#-----------------------------------------------------------------------------
# Console: Events
class EventsCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'events.add_events'
    
    def get_success_url(self):
        return reverse('console_events_detail', args=(self.object.pk,))

class EventsUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'events.change_events'
    
    def get_success_url(self):
        event = Event.objects.get(pk=self.object.pk)
        if event.state == core_constants.STATE_DELETED:
            return reverse('console_events_list')
        else:
            return reverse('console_events_detail', args=(self.object.pk,))

    def get_queryset(self):
        return Event.objects.exclude(state=core_constants.STATE_DELETED)

class EventsDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'events.change_events'

    def get_object(self):
        return get_object_or_404(
            Event, pk=self.kwargs['pk']
        )

class EventsDelete(AdminMixin, core_views.MarkDeleteView):
    permission_required = 'events.delete_events'
    
    def get_success_url(self):
        return reverse('console_events_list')

    def get_queryset(self):
        return Event.objects.all()

class EventsList(AdminMixin, generic_views.ListView):
    permission_required = 'events.change_events'
    
    def get_queryset(self):
        return Event.objects.exclude(state=core_constants.STATE_DELETED)
    
#-----------------------------------------------------------------------------
# Console: News
class NewsCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'news.add_news'
    
    def get_success_url(self):
        return reverse('console_news_detail', args=(self.object.pk,))

class NewsUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'news.change_news'
    
    def get_success_url(self):
        news = News.objects.get(pk=self.object.pk)
        if news.state == core_constants.STATE_DELETED:
            return reverse('console_news_list')
        else:
            return reverse('console_news_detail', args=(self.object.pk,))

    def get_queryset(self):
        return News.objects.exclude(state=core_constants.STATE_DELETED)

class NewsDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'news.change_news'

    def get_object(self):
        return get_object_or_404(
            News, pk=self.kwargs['pk']
        )

class NewsDelete(AdminMixin, core_views.MarkDeleteView):
    permission_required = 'news.delete_news'
    
    def get_success_url(self):
        return reverse('console_news_list')

    def get_queryset(self):
        return News.objects.exclude(state=core_constants.STATE_DELETED)

class NewsList(AdminMixin, generic_views.ListView):
    permission_required = 'news.change_news'
    
    def get_queryset(self):
        return News.objects.exclude(state=core_constants.STATE_DELETED)
    
#-----------------------------------------------------------------------------
# Console: Jobs
class JobsCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'jobs.add_jobs'
    
    def get_success_url(self):
        return reverse('console_jobs_detail', args=(self.object.pk,))

class JobsUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'jobs.change_jobs'
    
    def get_success_url(self):
        print '********************** Setting success url'
        job = JobPost.objects.get(pk=self.object.pk)
        print 'job', job
        if job.state == core_constants.STATE_DELETED:
            return reverse('console_jobs_list')
        else:
            return reverse('console_jobs_detail', args=(self.object.pk,))

    def get_queryset(self):
        return JobPost.objects.exclude(state=core_constants.STATE_DELETED)

class JobsDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'jobs.change_jobs'

    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            JobPost, pk=self.kwargs['pk']
        )

class JobsDelete(AdminMixin, core_views.MarkDeleteView):
    permission_required = 'jobs.delete_jobs'
    
    def get_success_url(self):
        return reverse('console_jobs_list')

    def get_queryset(self):
        return JobPost.objects.exclude(state=core_constants.STATE_DELETED)

class JobsList(AdminMixin, generic_views.ListView):
    permission_required = 'jobs.change_jobs'
    
    def get_queryset(self):
        return JobPost.objects.exclude(state=core_constants.STATE_DELETED)
    
 #-----------------------------------------------------------------------------
# Console: Gallery
class GalleryCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'gallery.add_gallery'
    
    def get_success_url(self):
        return reverse('console_gallery_detail', args=(self.object.pk,))

class GalleryUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'gallery.change_gallery'
    
    def get_success_url(self):
        gallery = Gallery.objects.get(pk=self.object.pk)
        if gallery.state == core_constants.STATE_DELETED:
            return reverse('console_gallery_list')
        else:
            return reverse('console_gallery_detail', args=(self.object.pk,))

    def get_queryset(self):
        return Gallery.objects.all()

class GalleryDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'gallery.change_gallery'

    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            Gallery, pk=self.kwargs['pk']
        )

class GalleryDelete(AdminMixin, core_views.MarkDeleteView):
    permission_required = 'gallery.delete_gallery'
    
    def get_success_url(self):
        return reverse('console_gallery_list')

    def get_queryset(self):
        return Gallery.objects.all()

class GalleryList(AdminMixin, generic_views.ListView):
    permission_required = 'gallery.change_gallery'
    
    def get_queryset(self):
        return Gallery.objects.all()
    
    
