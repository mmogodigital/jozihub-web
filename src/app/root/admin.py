'''
Created on 22 Oct 2013

@author: michael
'''
from django.contrib import admin

from app.root import models

admin.site.register(models.HeardAboutChoice)
admin.site.register(models.EventHostingChoice)
admin.site.register(models.TypeOfSpaceRequiredChoice)
admin.site.register(models.PartnerChoice)
admin.site.register(models.Application)