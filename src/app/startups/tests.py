from django.core.urlresolvers import reverse
from django.test import TestCase
from django.core import mail
from django.test.utils import override_settings
from django.conf import settings
from .models import StartupCompanies
from .views import Startup


class Startups(TestCase):

    def test_startup_view(self):

    	
        response = self.client.post(reverse('console_startups_create'),
                                    data={'name': 'foo',
                                    	  'rich_content': 'some txt',
                                          'founder_photographs': 'foo',
                                          'Link_to_their_website': 'foo.com',
                                          'social_media_profiles': '@foo',
                                          'contact_details': '0987654321',
                                          settings.HONEYPOT_FIELD_NAME: settings.HONEYPOT_VALUE})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(StartupCompanies.objects.count(), 1)
  
		