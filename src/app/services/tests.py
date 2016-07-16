from django.core.urlresolvers import reverse
from django.test import TestCase
from django.conf import settings
from .models import Services
from app.authentication.models import ProjectRegistrationProfile, EndUser

class Services(TestCase):
	def test_create_service_console(self):
		# register a user
		user = EndUser.objects.create_user(email='foo@example2.com', password='foo')
		user.is_superuser = True
		user.save()
		# login
		self.client.login(username='foo@example2.com', password='foo')
		response = self.client.post(
        	reverse('console_startups_create'),
            data={
                'title': 'foo',
                'slug': 'foo',
                'rich_content': 'some txt',
                settings.HONEYPOT_FIELD_NAME: settings.HONEYPOT_VALUE})


	def test_services_view(self):
		response = self.client.get(reverse('services'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Services.objects.count(), 1)


	def test_service_detail_view(self):
		response = self.client.get(reverse('services_details'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Services.objects.count(), 1)