from django.db import models
from time import time

def get_uplaad_file_name(instance, filename):
	return "uploads/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.


class startup_companies(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    logo = models.FileField(upload_to=get_uplaad_file_name)
    short_descriptor = models.TextField(blank=True, 
                                        null=True
                                       )
    long_descriptor = models.TextField(blank=True, 
                                       null=True
                                      )
    founder_photographs = models.TextField(max_length=120, blank=True, null=True)
    Link_to_their_website = models.TextField(max_length=120, blank=True, null=True)
    social_media_profiles = models.TextField(max_length=120, blank=True, null=True)
    contact_details = models.TextField(max_length=120, blank=True, null=True)
    rel_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name
