from django.core.urlresolvers import reverse
from django.test import TestCase
from django.conf import settings
from .models import Services
from app.authentication.models import ProjectRegistrationProfile, EndUser

class Services(TestCase):

	def test_services_view(self):
		response = self.client.get(reverse('services'))
		self.assertEqual(response.status_code, 200)
		