'''
Created on 26 Nov 2013

@author: christina
'''
from django import forms

from app.jobs import models

class PostJobForm(forms.ModelForm):
    class Meta:
        model = models.JobPost

    def __init__(self, *args, **kwargs):
        super(PostJobForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({'class': 'required'})
        self.fields['deadline'].widget.attrs.update({'class': 'required'})
        self.fields['description'].widget.attrs.update({
            'cols': '50', 'rows': '2',
            'class': 'required'
        })
