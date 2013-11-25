'''
Created on 25 Nov 2013

@author: michael
'''
from django import forms

from app.root import models

class ApplyForm(forms.ModelForm):
    class Meta:
        model = models.Application
        widgets = {
            'heard_about_from': forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super(ApplyForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update({'class': 'required'})
        self.fields['last_name'].widget.attrs.update({'class': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'required email'})