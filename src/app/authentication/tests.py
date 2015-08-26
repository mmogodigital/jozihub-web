from django.core.urlresolvers import reverse
from django.test import TestCase
from django.core import mail
from django.test.utils import override_settings
from django.conf import settings
from registration import signals as registration_signals


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class EmailTest(TestCase):

    def test_send_email(self):
        mail.send_mail('Copy for basic membership application',
                       'Here is the message.',
                       'info@jozihub.org', ['trevor@projectcodex.co'],
                       fail_silently=True)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject,
                          'Copy for basic membership application')

    def test_registration_view(self):
        response = self.client.post(reverse('secure_register'),
                                    data={'username': 'foo',
                                          'email': 'foo@example.com',
                                          'password1': 'foo',
                                          'password2': 'foo',
                                          settings.HONEYPOT_FIELD_NAME: settings.HONEYPOT_VALUE})
        self.assertEquals(len(mail.outbox), 1)
        self.assertEqual(response.status_code, 200)
        self.failUnless(response.context['form'])
        self.failUnless(response.context['form'].errors)
