'''
Created on 21 Oct 2013

@author: michael
'''
from django.views import generic as generic_views
from django.core.urlresolvers import reverse
from app.startups.models import StartupCompanies
from tunobase.corporate.media import models
from app.partners.models import Partner
from app.authentication.models import EndUser
from app.authentication.models import constants


class Index(generic_views.TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        events = models.Event.objects.all().count()
        

        context.update({
            'num_startups': StartupCompanies.objects.all().count(),
            'num_events': events,
            'num_partners': Partner.objects.all().count(),
            'num_mentors': EndUser.objects.filter(membership_type=constants.MENTOR_MEMBERSHIP).count(),
        })


        return context


class Apply(generic_views.CreateView):

    def get_success_url(self):
        return reverse('apply_success')


class ApplySuccess(generic_views.TemplateView):
    pass
