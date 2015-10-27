'''
Created on 21 Oct 2013

@author: michael
'''
from django.views import generic as generic_views
from django.core.urlresolvers import reverse
from app.startups.models import StartupCompanies


class Index(generic_views.TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)


        context.update({
            'num_startups': StartupCompanies.objects.all().count(),
        })


        return context


class Apply(generic_views.CreateView):

    def get_success_url(self):
        return reverse('apply_success')


class ApplySuccess(generic_views.TemplateView):
    pass
