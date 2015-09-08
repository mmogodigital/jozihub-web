'''
Created on 03 Dec 2013

@author: christina
'''
import csv

from django.core.urlresolvers import reverse
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.http import HttpResponse
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
from tunobase.corporate.media.models import Event

from app.authentication.models import EndUser
from app.console import forms
from app.jobs.models import JobPost
from app.news.models import News
from app.root import utils


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

    def form_invalid(self, form, **kwargs):
        print '*' * 10
        print dir(form)
        from pprint import pprint
        pprint(kwargs)
        pprint(form.errors)

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


class UserExport(generic_views.View):

    queryset = None

    def get(self, request, *args, **kwargs):

        if request.method == 'GET':
            kwargs = {}

            if request.GET.has_key('start_date'):
                kwargs['timestamp__gte'] = request.GET['start_date'].strip()

            if request.GET.has_key('end_date') and request.GET['end_date'].strip():
                kwargs['timestamp__lte'] = request.GET['end_date'].strip()

            queryset = self.queryset.filter(**kwargs)

            response = HttpResponse(mimetype='text/csv')
            response['Content-Disposition'] = 'attachment;filename=contact-inquiries.csv'
            writer = utils.UnicodeWriter(response)

            opts = queryset.model._meta
            field_names = [field.name for field in opts.fields]
            field_names.remove('last_login')
            field_names.remove('username')
            field_names.remove('is_superuser')
            field_names.remove('image')
            field_names.remove('date_taken')
            field_names.remove('view_count')
            field_names.remove('crop_from')
            field_names.remove('effect')
            field_names.remove('title')
            field_names.remove('age')
            field_names.remove('job_title')
            field_names.remove('company')
            field_names.remove('phone_number')
            field_names.remove('date_joined')
            field_names.remove('street_address')
            field_names.remove('city')
            field_names.remove('state_province')
            field_names.remove('zip_postal_code')
            field_names.remove('country')
            field_names.remove('web_address')
            field_names.remove('is_regular_user')
            field_names.remove('is_active')
            field_names.remove('is_admin')
            field_names.remove('is_console_user')
            field_names.remove('heard_about_from_other')
            field_names.remove('submit_reason')
            field_names.remove('information_about_jozihub')
            field_names.remove('educational_background')
            field_names.remove('about_you')
            field_names.remove('events_interested_in_hosting_other')
            field_names.remove('when_to_host_event')
            field_names.remove('required_from_us')
            field_names.remove('how_can_you_contribute_to_jozihub')
            field_names.remove('aims_to_get_from_jozihub')
            field_names.remove('when_to_get_access')
            field_names.remove('happy_with_the_price')
            field_names.remove('become_a_partner_or_funder_other')
            field_names.remove('about_your_organisation')
            field_names.remove('what_do_you_aim_to_achieve')
            field_names.remove('partnership_expectation')
            field_names.remove('field_of_expertise')
            field_names.remove('field_of_expertise_other')
            field_names.remove('background_and_expertise')
            field_names.remove('what_can_you_offer_as_a_mentor')
            field_names.remove('mentoring_time')
            field_names.remove('password')

            writer.writerow(field_names)

            for obj in queryset:
                writer.writerow([getattr(obj, field) for field in field_names])
            return response


#-----------------------------------------------------------------------------
# Console: Events
class EventsCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'events.add_events'

    def get_success_url(self):
        return reverse('console_events_detail', args=(self.object.pk,))


class EventsUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'events.change_events'

    def form_invalid(self, form):
        print '*' * 10
        print form.errors

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
        job = JobPost.objects.get(pk=self.object.pk)
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

# Flatpages

class FlatPagesList(AdminMixin, generic_views.ListView):
    permission_required = 'blogs.blogs_list'

    def get_queryset(self):
        return FlatPage.objects.filter(
            sites=Site.objects.get_current(),
        )

class FlatPagesDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'parters.partners_update'

    def get_object(self):
        return get_object_or_404(
            FlatPage,
            pk=self.kwargs['pk'],
            sites=Site.objects.get_current(),
        )

class FlatPagesUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'partners.partners_update'

    def get_success_url(self):
        return reverse('console_flatpage_detail', args=(self.object.pk,))

    def get_queryset(self):
        return FlatPage.objects.filter(
            sites=Site.objects.get_current(),
        )
