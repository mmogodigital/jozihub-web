from django.core.urlresolvers import reverse
from django.test import TestCase
from django.core import mail
from django.test.utils import override_settings
from django.conf import settings
from .models import ProjectRegistrationProfile


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend', USE_CELERY=False)
class EmailTest(TestCase):

    def test_registration_view(self):
        response = self.client.post(reverse('secure_register'),
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
        self.assertEquals(len(mail.outbox), 1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'],
                         'http://testserver%s' %
                         reverse('registration_complete'))

    def test_activation_view(self):

        response = self.client.post(
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

        response = self.client.get(reverse('secure_activate', kwargs={
            'activation_key': ProjectRegistrationProfile.objects.get(
                user__email='foo@example2.com').activation_key}))
        self.assertEquals(len(mail.outbox), 2)
        self.assertEquals(
            mail.outbox[1].subject, 'Copy for basic membership application')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['Location'],
            'http://testserver%s' %
            reverse('registration_activation_complete'))
