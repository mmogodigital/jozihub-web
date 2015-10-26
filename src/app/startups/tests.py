from django.core.urlresolvers import reverse
from django.test import TestCase
from django.conf import settings
from .models import StartupCompanies
from app.authentication.models import ProjectRegistrationProfile, EndUser


class Startups(TestCase):

    def test_startup_view(self):

        # register a user
        self.client.post(
            reverse('secure_register'),
            data={'username': 'foo',
                  'first_name': 'foo',
                  'last_name': 'foo',
                  'email': 'foo@example2.com',
                  'password1': 'foo',
                  'password2': 'foo',
                  'field_of_expertise': 1,
                  'when_to_host_event': 1,
                  'information_about_jozihub': 1,
                  'when_to_get_access': 1,
                  'happy_with_the_price': 1,
                  settings.HONEYPOT_FIELD_NAME: settings.HONEYPOT_VALUE})

        self.client.get(reverse('secure_activate', kwargs={
            'activation_key': ProjectRegistrationProfile.objects.get(
                user__email='foo@example2.com').activation_key}))
        # give user admin permissions
        user = EndUser.objects.get(email='foo@example2.com')
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
