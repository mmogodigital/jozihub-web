from django.core.urlresolvers import reverse
from django.test import TestCase
from django.core import mail
from django.test.utils import override_settings
from django.conf import settings


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend', USE_CELERY=False)
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
        print response
        self.assertEquals(len(mail.outbox), 1)
        self.assertEqual(response.status_code, 200)
        self.failUnless(response.context['form'])
        self.failUnless(response.context['form'].errors)
