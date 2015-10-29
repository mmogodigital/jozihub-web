import collections
from django.conf import settings
from django import forms

from app.events import tasks

# Profile Update Form

class VenueHireForm(forms.Form):
    CHOICES = [('jozihubboardroom', 'JoziHub Board Room'),
               ('jozihubmaineventspace', 'JoziHub Main Event Space')]
    accepted_date_formats = ['%d-%m-%Y']
    accepted_time_formats = ['%I:%M-%p',
                             '%I:%M - %p',
                             '%I : %M-%p',
                             '%I : %M - %p']

    eventname = forms.CharField(label='Event Name')
    eventdescription = forms.CharField(widget=forms.Textarea,
                                       label='Event Description')
    contactname = forms.CharField(label='Name')
    contactemail = forms.EmailField(label='Email')
    contactnumber = forms.CharField(label='Contact Number')
    contactcompany = forms.CharField(label='Company')
    startdate = forms.DateField(input_formats=accepted_date_formats,
                                label='Venue Booking Start Date')
    starttime = forms.TimeField(input_formats=accepted_time_formats,
                                label='Venue Booking Start Time')
    enddate = forms.DateField(input_formats=accepted_date_formats,
                              label='Venue Booking End Date')
    endtime = forms.TimeField(input_formats=accepted_time_formats,
                              label='Venue Booking End Time')
    desiredvenue = forms.ChoiceField(label='Desired Venue', choices=CHOICES)
        
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        context = self.cleaned_data
        venue_name = ""
        for (id,name) in self.CHOICES:
            if id == context['desiredvenue']:
                venue_name = name
                break
        context['desiredvenue_name'] = venue_name
        if settings.USE_CELERY:
            tasks.email_venue_hire.delay(context)
        else:
            tasks.email_venue_hire(context)
        pass

