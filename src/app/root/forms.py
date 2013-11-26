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
            'heard_about_from': forms.CheckboxSelectMultiple,
            'events_interesting_in_hosting': forms.CheckboxSelectMultiple,
            'type_of_space_required': forms.CheckboxSelectMultiple,
            'become_a_partner_or_funder': forms.CheckboxSelectMultiple,
            'information_about_jozihub': forms.RadioSelect(),
            'when_to_host_event': forms.RadioSelect(),
            'field_of_expertise': forms.RadioSelect(),
            'when_to_get_access': forms.RadioSelect(),
            'happy_with_the_price': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(ApplyForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update({'class': 'required'})
        self.fields['last_name'].widget.attrs.update({'class': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'required email'})
        
        self.fields['about_you'].widget.attrs.update({'cols': '50', 'rows': '2'})
        self.fields['educational_background'].widget.attrs.update({'cols': '50', 'rows': '2'})
        self.fields['required_from_us'].widget.attrs.update({'cols': '50', 'rows': '2'})
        self.fields['how_can_you_contribute_to_jozihub'].widget.attrs.update({'cols': '50', 'rows': '2'})
        self.fields['aims_to_get_from_jozihub'].widget.attrs.update({'cols': '50', 'rows': '2'})
        
        self.fields['about_your_organisation'].widget.attrs.update({'cols': '50', 'rows': '2'})
        self.fields['what_do_you_aim_to_achieve'].widget.attrs.update({'cols': '50', 'rows': '2'})
        self.fields['partnership_expectation'].widget.attrs.update({'cols': '50', 'rows': '2'})
        self.fields['background_and_expertise'].widget.attrs.update({'cols': '50', 'rows': '2'})
        self.fields['what_can_you_offer_as_a_mentor'].widget.attrs.update({'cols': '50', 'rows': '2'})