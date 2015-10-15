from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.core import mail
from django.test.client import Client
from django.test.utils import override_settings
from django.conf import settings
from .models import StartupCompanies
from .views import Startup


class Startups(TestCase):

	def test_startup_view(self):

		# self.user = User.objects.create_user(username ='trevor@praekeltconsulting.com',
	 #        								 password ='trevor332')

	 #    self.client.post(reverse('secure_login'), 
	 #    				 data={'username': 'trevor@praekeltconsulting.com',
	 #        				   'password': 'trevor332',
	 #        				   'next': '/console/startups/create/'})

	 #    self.assertEqual(response['Location'],'http://testserver/console/startups/create/')

		# response = self.client.post(reverse('secure_login'),
		#                             data={'username': 'trevor@praekeltconsulting.com',
		#                             	  'password': 'pass332',
		#                                   'next': '/console/startups/create/',
		#                                   settings.HONEYPOT_FIELD_NAME: settings.HONEYPOT_VALUE})
		response = self.client.login(username='trevor@praekeltconsulting.com', password='pass332')

		response = self.client.post(reverse('console_startups_create'),
									data={'name': 'foo',
										  'rich_content': 'some txt',
										  'founder_photographs': 'foo',
										  'Link_to_their_website': 'foo.com',
										  'social_media_profiles': '@foo',
										  'contact_details': '0987654321',
										  'next': '/console/startups/1/detail/',
										  settings.HONEYPOT_FIELD_NAME: settings.HONEYPOT_VALUE})

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['Location'],'http://testserver/console/startups/1/detail/')
		