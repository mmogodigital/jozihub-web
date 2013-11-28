'''
Created on 26 Nov 2013

@author: christina
'''
from django import forms

from app.jobs import models

class PostJobForm(forms.ModelForm):
    class Meta:
        model = models.JobPost
        widgets = {
            'job_categories': forms.CheckboxSelectMultiple,
        }
