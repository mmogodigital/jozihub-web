'''
Created on 3 Dec 2013

@author: christina
'''
from django import forms

from app.events.models import Event
from app.authentication.models import EndUser
from app.news.models import News
from app.jobs.models import JobPost
        
class EventsForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = [
                'image', 'title', 'start', 'end', 'venue_name', 'venue_address',
                'repeat', 'repeat_until', 'external_link', 'calendar_link',
        ]

class UsersForm(forms.ModelForm):
    
    class Meta:
        model = EndUser
        exclude = [
                'job_title', 'company', 'username', 'date_joined',
                'street_address', 'state_province', 'zip_postal_code',
                'country', 'web_address', 'is_regular_user', 'is_active',
                'is_admin', 'is_console_user'
        ]

class NewsForm(forms.ModelForm):
    
    class Meta:
        model = News
        fields = [
                'state', 'title', 'rich_content', 'image'
        ]

class JobsForm(forms.ModelForm):
    
    class Meta:
        model = JobPost
        fields = [
                'state', 'title', 'location', 'application_date', 'description',
        ]
