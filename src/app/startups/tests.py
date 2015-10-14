from django.core.urlresolvers import reverse
from django.test import TestCase
from django.core import mail
from django.test.utils import override_settings
from django.conf import settings
from .models import StartupCompanies


class EmailTest(TestCase):

    # def test_startup_view(self):
    #     response = self.client.get(reverse('startups'),
    #                                 data={'name': 'foo',
    #                                       'founder_photographs': 'foo',
    #                                       'Link_to_their_website': 'foo.com',
    #                                       'social_media_profiles': '@foo',
    #                                       'contact_details': '0987654321',
    #                                       settings.HONEYPOT_FIELD_NAME: settings.HONEYPOT_VALUE})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(StartupCompanies.objects.count(), 1)

    def test_startups(self):
    	startup = StartupCompanies.objects.create(name="foo", founder_photographs="foo",
    											  Link_to_their_website="foo.com", social_media_profiles="@foo",
    											  contact_details="0987654321")
    	self.assertEqual(startup.pk, 1)
    	self.assertEqual(startup.name, 'foo')
