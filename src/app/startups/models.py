from django.db import models
from tunobase.core import models as core_models

# Create your models here.


class StartupCompanies(core_models.BaseContentModel):
    name = models.CharField(max_length=120, blank=True, null=True)
    founder_photographs = models.TextField(max_length=120, blank=True, null=True)
    Link_to_their_website = models.TextField(max_length=120, blank=True, null=True)
    social_media_profiles = models.TextField(max_length=120, blank=True, null=True)
    contact_details = models.TextField(max_length=120, blank=True, null=True)
