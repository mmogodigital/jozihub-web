'''
Created on 3 Dec 2013

@author: christina
'''
from django import forms

from app.events import models
        
class EventsForm(forms.ModelForm):
    
    class Meta:
        model = models.Event

class UsersForm(forms.ModelForm):
    
    class Meta:
        model = models.Event
