'''
Created on 16 July 2016

@author: Tawanda
'''
from django.contrib import admin

from app.services import models

admin.site.register(models.Services)