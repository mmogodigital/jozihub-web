'''
Created on 16 Jan 2013

@author: euan
'''
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage

#==============================================================================
class Command(BaseCommand):
    """
    Initial base setup
    """
    #--------------------------------------------------------------------------
    def handle(self, *args, **options):
        # Sites
        print 'Defaulting site to localhost:8000'
        site = Site.objects.get_current()
        site.domain = 'localhost:8000'
        site.name = 'localhost'
        site.save()
        
        # Flatpages
        print 'Creating Flatpages'
        site = Site.objects.get_current()
        
        terms = FlatPage.objects.create(
            url='/membership-terms/',
            title='Membership Terms',
            content='<p>Terms &amp; Conditions</p>'
        )
        terms.sites.add(site)
        
        privacy_policy = FlatPage.objects.create(
            url='/data-protection-policy/',
            title='Data Protection Policy',
            content='<p>Privacy Policy</p>'
        )
        privacy_policy.sites.add(site)
        
        code_of_conduct = FlatPage.objects.create(
            url='/code-of-conduct/',
            title='Code of Conduct',
            content='<p>Code</p>'
        )
        code_of_conduct.sites.add(site)