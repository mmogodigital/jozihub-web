'''
Created on 3 Dec 2013

@author: christina
'''
from django import forms

from tunobase.core.models import Gallery

from app.authentication.models import EndUser
from app.events.models import Event
from app.jobs.models import JobPost
from app.news.models import News
        
class UsersForm(forms.ModelForm):
    
    class Meta:
        model = EndUser
        exclude = [
                'job_title', 'company', 'username', 'date_joined',
                'street_address', 'state_province', 'zip_postal_code',
                'country', 'web_address', 'is_regular_user', 'is_active',
                'is_admin', 'is_console_user', 'password', 'last_login'
        ]

class EventsForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = [
                'image', 'title', 'start', 'end', 'venue_name', 'venue_address',
                'repeat', 'repeat_until', 'external_link', 'calendar_link',
                'state', 'rich_content',
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

class GalleryForm(forms.ModelForm):
    
    class Meta:
        model = Gallery
        fields = [
                'state', 'title', 'rich_content', 'images',
        ]