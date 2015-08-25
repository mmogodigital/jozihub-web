from django.test import TestCase
from django.core import mail
from django.test.utils import override_settings


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
