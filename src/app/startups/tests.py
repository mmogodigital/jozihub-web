from django.core.urlresolvers import reverse
from django.test import TestCase
from django.conf import settings
from .models import StartupCompanies
from app.authentication.models import ProjectRegistrationProfile, EndUser


class Startups(TestCase):

    def test_startup_view(self):

        # register a user
        user = EndUser.objects.create_user(email='foo@example2.com', password='foo')
        user.is_superuser = True
        user.save()

        # login
        self.client.login(username='foo@example2.com', password='foo')

        response = self.client.post(
            reverse('console_startups_create'),
            data={
                'name': 'foo',
                'rich_content': 'some txt',
                'founder_photographs': 'foo',
                'Link_to_their_website': 'foo.com',
                'social_media_profiles': '@foo',
                'contact_details': '0987654321',
                settings.HONEYPOT_FIELD_NAME: settings.HONEYPOT_VALUE})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(StartupCompanies.objects.count(), 1)
