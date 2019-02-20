from django.db import models
# Create your models here.


class StartUp(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    founder_photographs = models.TextField(max_length=120, blank=True, null=True)
    website = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    twitter = models.CharField(max_length=120, blank=True, null=True)
    linkedin = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)
    blog = models.CharField(max_length=120, blank=True, null=True)
    contact_details = models.TextField(max_length=120, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    image = models.ImageField(upload_to='static/media/startups')

    def __str__(self):
    	return self.title
