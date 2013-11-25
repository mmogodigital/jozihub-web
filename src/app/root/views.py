'''
Created on 21 Oct 2013

@author: michael
'''
from django.views import generic as generic_views
from django.core.urlresolvers import reverse

class Index(generic_views.TemplateView):
    pass

class Apply(generic_views.CreateView):
    
    def get_success_url(self):
        return reverse('apply_success')
    
class ApplySuccess(generic_views.TemplateView):
    pass