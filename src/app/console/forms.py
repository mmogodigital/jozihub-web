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
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput, required=False)

    class Meta:
        model = EndUser
        exclude = [
                'job_title', 'company', 'username', 'date_joined',
                'street_address', 'state_province', 'zip_postal_code',
                'country', 'web_address', 'is_regular_user', 'is_active',
                'is_admin', 'is_console_user', 'password', 'last_login'
        ]

    def clean_email(self):
        """
        We don't do any checking to confirm that their 'new' email address
        isn't already taken, so don't allow the user to change their email
        address.
        """
        if self.instance.id:
            if self.instance.email != self.cleaned_data['email']:
                raise forms.ValidationError(
                        "You cannot change your email address"
                )

    def clean_password2(self):
        if ('password1' in self.cleaned_data and
                'password2' in self.cleaned_data):
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords didn't match.")

    def save(self, commit=True):
        obj = super(UsersForm, self).save(commit)

        if self.clean_data['password1']:
            obj.set_password(self.cleaned_data['password1'])

        obj.save()

        return obj

class UserFilter(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)

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
