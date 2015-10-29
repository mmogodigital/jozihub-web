import collections
from django.conf import settings
from django import forms

from app.events import tasks

# Profile Update Form

class VenueHireForm(forms.Form):
    CHOICES = [('jozihubboardroom', 'JoziHub Board Room'),
               ('jozihubmaineventspace', 'JoziHub Main Event Space')]
    eventname = forms.CharField(label='Event Name')
    eventdescription = forms.CharField(widget=forms.Textarea,
                                       label='Event Description')
    contactname = forms.CharField(label='Name')
    contactemail = forms.EmailField(label='Email')
    contactnumber = forms.CharField(label='Contact Number')
    contactcompany = forms.CharField(label='Company')
    startdate = forms.DateField(label='Venue Booking Start Date')
    starttime = forms.TimeField(label='Venue Booking Start Time')
    enddate = forms.DateField(label='Venue Booking End Date')
    endtime = forms.TimeField(label='Venue Booking End Time')
    desiredvenue = forms.ChoiceField(label='Desired Venue', choices=CHOICES)
        
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        context = self.cleaned_data
        if settings.USE_CELERY:
            tasks.email_venue_hire.delay(context)
        else:
            tasks.email_venue_hire(context)
        pass

