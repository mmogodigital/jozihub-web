'''
Created on 25 Nov 2013

@author: michael
'''
from django.contrib import admin

from app.partners import models

admin.site.register(models.Partner)