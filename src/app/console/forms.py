'''
Created on 3 Dec 2013

@author: christina
'''
from django import forms
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site

from ckeditor.widgets import CKEditorWidget

from tunobase.core.models import Gallery
from tunobase.corporate.media.models import Event

from app.authentication.models import EndUser
from app.jobs.models import JobPost
from app.news.models import News
from app.startups.models import StartupCompanies
from app.partners.models import Partner
from app.services.models import Services

class UsersForm(forms.ModelForm):
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput, required=False)

    class Meta:
        model = EndUser
        exclude = [
                'username', 'date_joined',
                'street_address', 'state_province', 'zip_postal_code',
                'country', 'web_address', 'is_regular_user', 'is_active',
                'is_admin', 'is_console_user', 'password', 'last_login',
        ]

    def __init__(self, *args, **kwargs):
        super(UsersForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['email'].widget.attrs['readonly'] = True
        else:
            self.fields['email'].widget.attrs.update({
                'class': 'required email',
            })

        self.fields['first_name'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'number',
        })
        self.fields['age'].widget.attrs.update({
            'class': 'number',
        })

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
        return self.cleaned_data['email']

    def clean_password2(self):
        if ('password1' in self.cleaned_data and
                'password2' in self.cleaned_data):
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords didn't match.")

    def save(self, commit=True):
        obj = super(UsersForm, self).save(commit)

        if self.cleaned_data['password1']:
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
        widgets = {
                'image': forms.FileInput
        }

    def __init__(self, *args, **kwargs):
        super(EventsForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs:
            self.object = kwargs['instance']

        self.fields['start'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['venue_address'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['venue_name'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['title'].widget.attrs.update({
            'class': 'required',
        })

    def save(self, commit=True):
        obj = super(EventsForm, self).save(commit)
        obj.sites.add(1)
        obj.save()
        return obj


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = [
                'state', 'title', 'rich_content', 'image'
        ]
        widgets = {
                'image': forms.FileInput
        }

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs:
            self.object = kwargs['instance']

        self.fields['title'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['rich_content'].widget.attrs.update({
            'class': 'required',
        })

    def save(self, commit=True):
        obj = super(NewsForm, self).save(commit)
        obj.sites.add(1)
        obj.save()
        return obj

class JobsForm(forms.ModelForm):

    class Meta:
        model = JobPost
        fields = [
                'state', 'title', 'location', 'application_date', 'description',
        ]

    def __init__(self, *args, **kwargs):
        super(JobsForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs:
            self.object = kwargs['instance']

        self.fields['title'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['application_date'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['description'].widget.attrs.update({
            'class': 'required',
        })

    def save(self, commit=True):
        obj = super(JobsForm, self).save(commit)
        obj.sites.add(1)
        obj.save()
        return obj

class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = [
                'state', 'image', 'title', 'rich_content', 'images',
        ]
        widgets = {
                'image': forms.FileInput
        }

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs:
            self.object = kwargs['instance']

        self.fields['title'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['images'].widget.attrs.update({
            'class': 'required',
        })

    def save(self, commit=True):
        obj = super(GalleryForm, self).save(commit)
        obj.sites.add(1)
        obj.save()
        return obj

class StartupForm(forms.ModelForm):

    class Meta:
        model = StartupCompanies
        fields = [
                'image', 'name', 'founder_photographs', 'title',
                'Link_to_their_website', 'social_media_profiles',
                'contact_details', 'rich_content',
        ]
        widgets = {
                'logo': forms.FileInput
        }

    def __init__(self, *args, **kwargs):
        super(StartupForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs:
            self.object = kwargs['instance']

        self.fields['title'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'required',
        })

    def save(self, commit=True):
        obj = super(StartupForm, self).save(commit)
        sites=Site.objects.get_current(),
        obj.save()
        return obj

class PartnerForm(forms.ModelForm):

    class Meta:
        model = Partner
        fields = [
                'image', 'title', 'rich_content',
                'external_link',
        ]
        widgets = {
                'image': forms.FileInput
        }

    def __init__(self, *args, **kwargs):
        super(PartnerForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs:
            self.object = kwargs['instance']

        self.fields['title'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'required',
        })

    def save(self, commit=True):
        obj = super(PartnerForm, self).save(commit)
        sites=Site.objects.get_current(),
        obj.save()
        return obj

class FlatPageForm(forms.ModelForm):

    class Meta:
        model = FlatPage
        fields = ['title', 'content']
        widgets = {
            'content': CKEditorWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(FlatPageForm, self).__init__(*args, **kwargs)


        self.fields['title'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['content'].widget.attrs.update({
            'class': 'required',
        })

    def save(self, commit=True):
        obj = super(FlatPageForm, self).save(commit)
        obj.sites.add(Site.objects.get_current())
        obj.save()
        return obj


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = [
                'image', 'title', 'rich_content',
                'order',
        ]
        widgets = {
                'image': forms.FileInput
        }

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs:
            self.object = kwargs['instance']

        self.fields['title'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'required',
        })

    def save(self, commit=True):
        obj = super(ServiceForm, self).save(commit)
        sites=Site.objects.get_current(),
        obj.save()
        return obj