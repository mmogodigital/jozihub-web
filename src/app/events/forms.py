import collections
from django.conf import settings
from django import forms

from app.events import tasks

# Profile Update Form

class VenueHireForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    contact_email = forms.EmailField()
    affiliated_organisation = forms.CharField(required=False)
    # event_start_time = forms.DateTimeField(widget=forms.DateTimeInput)
    # event_end_time = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
    event_description = forms.CharField(widget=forms.Textarea)
        
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        context = convert_to_utf8(self.cleaned_data)
        if settings.USE_CELERY:
            tasks.email_venue_hire.delay(context)
        else:
            tasks.email_venue_hire(context)
        pass

def convert_to_utf8(data):
    if isinstance(data, basestring):
        return data.encode("utf8")
    elif isinstance(data, collections.Mapping):
        return dict(map(convert_to_utf8, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert_to_utf8, data))
    else:
        return data
