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
from app.startups.models import StartupCompanies
from app.partners.models import Partner
from app.root import utils


class AdminMixin(
    console_mixins.ConsoleUserRequiredMixin,
    core_mixins.PermissionRequiredMixin
):
    raise_exception = False


class ConsoleLanding(AdminMixin, TemplateView):
    permission_required = 'events.add_events'


# ----------------------------------------------------------------------------
# Console: Users
class UsersCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'users.add_users'

    def get_success_url(self):
        return reverse('console_users_detail', args=(self.object.pk,))


class UsersUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'users.change_users'

    def form_invalid(self, form):
        print '*' * 10
        print form
        return super(UsersUpdate, self).form_invalid(form)

    def get_success_url(self):
        user = EndUser.objects.get(pk=self.object.pk)
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

            excluded_fields = [
                'id', 'last_login', 'username', 'is_superuser',
                'image', 'date_taken', 'view_count',
                'crop_from', 'effect', 'title', 'age',
                'job_title', 'company', 'phone_number',
                'date_joined', 'street_address', 'city',
                'state_province', 'zip_postal_code', 'country',
                'web_address', 'is_regular_user', 'is_active',
                'is_console_user', 'heard_about_from_other',
                'submit_reason', 'information_about_jozihub',
                'educational_background', 'about_you',
                'events_interested_in_hosting_other',
                'when_to_host_event', 'required_from_us',
                'how_can_you_contribute_to_jozihub',
                'aims_to_get_from_jozihub',
                'when_to_get_access', 'happy_with_the_price',
                'become_a_partner_or_funder_other',
                'about_your_organisation',
                'what_do_you_aim_to_achieve',
                'partnership_expectation', 'field_of_expertise',
                'field_of_expertise_other',
                'background_and_expertise',
                'what_can_you_offer_as_a_mentor',
                'mentoring_time', 'password', 'affiliation']

            for field in excluded_fields:
                field_names.remove(field)

            writer.writerow(field_names)

            for obj in queryset:
                writer.writerow([getattr(obj, field) for field in field_names])
            return response


# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# Console: Startup
class StartupCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'startups.add_startups'

    def get_success_url(self):
        return reverse('console_startups_detail', args=(self.object.pk,))


class StartupUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'startups.change_startups'

    def get_success_url(self):
        startups = StartupCompanies.objects.get(pk=self.object.pk)
        if startups.state == core_constants.STATE_DELETED:
            return reverse('console_startups_list')
        else:
            return reverse('console_startups_detail', args=(self.object.pk,))

    def get_queryset(self):
        return StartupCompanies.objects.exclude(state=core_constants.STATE_DELETED)


class StartupDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'startups.change_startups'

    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            StartupCompanies, pk=self.kwargs['pk']
        )


class StartupDelete(AdminMixin, core_views.MarkDeleteView):
    permission_required = 'startups.delete_startups'

    def get_success_url(self):
        return reverse('console_startups_list')

    def get_queryset(self):
        return StartupCompanies.objects.exclude(state=core_constants.STATE_DELETED)


class StartupList(AdminMixin, generic_views.ListView):
    permission_required = 'startups.change_startups'

    def get_queryset(self):
        return StartupCompanies.objects.exclude(state=core_constants.STATE_DELETED)

# -----------------------------------------------------------------------------
# Console: Partners
class PartnerCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'partners.add_partners'

    def get_success_url(self):
        return reverse('console_partners_detail', args=(self.object.pk,))


class PartnerUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'partners.change_partners'

    def get_success_url(self):
        partners = Partner.objects.get(pk=self.object.pk)
        if partners.state == core_constants.STATE_DELETED:
            return reverse('console_partners_list')
        else:
            return reverse('console_partners_detail', args=(self.object.pk,))

    def get_queryset(self):
        return Partner.objects.exclude(state=core_constants.STATE_DELETED)


class PartnerDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'partners.change_partners'

    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            Partner, pk=self.kwargs['pk']
        )


class PartnerDelete(AdminMixin, core_views.MarkDeleteView):
    permission_required = 'partners.delete_partners'

    def get_success_url(self):
        return reverse('console_partners_list')

    def get_queryset(self):
        return Partner.objects.exclude(state=core_constants.STATE_DELETED)


class PartnerList(AdminMixin, generic_views.ListView):
    permission_required = 'partners.change_partners'

    def get_queryset(self):
        return Partner.objects.exclude(state=core_constants.STATE_DELETED)

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
