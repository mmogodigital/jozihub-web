'''
Created on 26 Nov 2013

@author: christina
'''
from django.contrib import admin

from app.jobs import models

admin.site.register(models.JobPost)
