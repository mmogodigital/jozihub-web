from django.conf import settings
from django import forms
from django.contrib.sites.models import get_current_site
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.tokens import default_token_generator
from django.template import loader
from django.utils.http import int_to_base36
from django.template.loader import render_to_string
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from app.authentication import signals, constants, models
from app.root import constants as root_constants

# Profile Update Form

class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = get_user_model()
        fields = [
            'title', 'first_name', 'last_name', 
            'email', 'phone_number', 'mobile_number',
            'image', 'country', 'city', 'street_address',
            'state_province', 'zip_postal_code', 'web_address'
        ]
        
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({'class': 'required'})
        self.fields['first_name'].widget.attrs.update({'class': 'required'})
        self.fields['last_name'].widget.attrs.update({'class': 'required'})
        self.fields['email'].widget.attrs.update({'readonly': 'readonly'})
        
        
    def clean_email(self):
        '''
        Validate that the supplied email address is unique for the
        site.
        '''
        if get_user_model().objects.filter(email__iexact=self.cleaned_data['email'])\
           .exclude(email__iexact=self.instance.email).exists():
            raise forms.ValidationError(
                'This email address is already in use. '
                'Please supply a different email address.'
            )
            
        return self.cleaned_data['email']
    
class UpdateProfilePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, user, *args, **kwargs):
        super(UpdateProfilePasswordForm, self).__init__(*args, **kwargs)
        self.user = user
        
    def clean_old_password(self):
        '''
        Verify that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        '''
        if not self.user.check_password(self.cleaned_data['old_password']):
            raise forms.ValidationError('The password supplied does not match your current password.')
                
        return self.cleaned_data['old_password']
        
    def clean_password2(self):
        '''
        Verify that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        '''
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] and self.cleaned_data['password2']:
                if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                    raise forms.ValidationError('The password fields didn\'t match: Password confirmation failed.')
            return self.cleaned_data['password2']

    def clean(self):
        '''
        Verify that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        '''
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] and self.cleaned_data['password2']:
                if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                    raise forms.ValidationError('The two password fields didn\'t match.')
        return self.cleaned_data
        
    def save(self):
        self.user.set_password(self.cleaned_data['password1'])
        self.user.save()

# Registration forms

class ProjectRegistrationForm(forms.ModelForm):
    '''
    Form for registering a new user account.
    
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.
    '''
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    when_to_host_event = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=root_constants.WHEN_TO_HOST_EVENT_CHOICES,
    )
    when_to_get_access = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=root_constants.WHEN_TO_GET_ACCESS_CHOICES,
    )
    happy_with_the_price = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=root_constants.HAPPY_WITH_THE_PRICE_CHOICES,
    )
    field_of_expertise = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=root_constants.FIELD_OF_EXPERTISE_CHOICES,
    )

    
    def clean_email(self):
        '''
        Validate that the supplied email address is unique for the
        site.
        '''
        if get_user_model().objects.filter(email__iexact=self.cleaned_data['email']).exists():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        
        return self.cleaned_data['email']

    def clean_password2(self):
        '''
        Verify that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        '''
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] and self.cleaned_data['password2']:
                if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                    raise forms.ValidationError('The password fields didn\'t match: Password confirmation failed.')
            return self.cleaned_data['password2']

    def clean(self):
        '''
        Verify that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        '''
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] and self.cleaned_data['password2']:
                if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                    raise forms.ValidationError('The two password fields didn\'t match.')
        return self.cleaned_data

    class Meta:
        model = models.EndUser
        fields = [
                'first_name', 'last_name', 'email', 'phone_number', 'age',
                'city', 'heard_about_from', 'heard_about_from_other',
                'affiliation', 'submit_reason', 'information_about_jozihub',
                'educational_background', 'about_you',
                'events_interested_in_hosting',
                'events_interested_in_hosting_other', 'when_to_host_event',
                'required_from_us', 'how_can_you_contribute_to_jozihub',
                'aims_to_get_from_jozihub', 'when_to_get_access',
                'type_of_space_required','happy_with_the_price',
                'become_a_partner_or_funder',
                'become_a_partner_or_funder_other', 'about_your_organisation',
                'what_do_you_aim_to_achieve', 'partnership_expectation',
                'field_of_expertise', 'field_of_expertise_other',
                'background_and_expertise', 'what_can_you_offer_as_a_mentor',
                'mentoring_time',
        ]
        widgets = {
            'heard_about_from': forms.CheckboxSelectMultiple,
            'events_interesting_in_hosting': forms.CheckboxSelectMultiple,
            'type_of_space_required': forms.CheckboxSelectMultiple,
            'become_a_partner_or_funder': forms.CheckboxSelectMultiple,
            'information_about_jozihub': forms.RadioSelect(),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectRegistrationForm, self).__init__(*args, **kwargs)

        self.user = None

        self.fields['first_name'].widget\
                .attrs.update({'class':'required'})
        self.fields['last_name'].widget\
                .attrs.update({'class':'required'})
        self.fields['email'].widget\
                .attrs.update({'class':'required email'})
        self.fields['password1'].widget\
                .attrs.update({'class':'required'})
        self.fields['password2'].widget\
                .attrs.update({'class':'required'})
        self.fields['about_you'].widget\
                .attrs.update({'cols': '50', 'rows': '2'})
        self.fields['educational_background'].widget\
                .attrs.update({'cols': '50', 'rows': '2'})
        self.fields['required_from_us'].widget\
                .attrs.update({'cols': '50', 'rows': '2'})
        self.fields['how_can_you_contribute_to_jozihub'].widget\
                .attrs.update({'cols': '50', 'rows': '2'})
        self.fields['aims_to_get_from_jozihub'].widget\
                .attrs.update({'cols': '50', 'rows': '2'})
        self.fields['about_your_organisation'].widget\
                .attrs.update({'cols': '50', 'rows': '2'})
        self.fields['what_do_you_aim_to_achieve'].widget\
                .attrs.update({'cols': '50', 'rows': '2'})
        self.fields['partnership_expectation'].widget\
                .attrs.update({'cols': '50', 'rows': '2'})
        self.fields['background_and_expertise'].widget\
                .attrs.update({'cols': '50', 'rows': '2'})
        self.fields['what_can_you_offer_as_a_mentor'].widget\
                .attrs.update({'cols': '50', 'rows': '2'})
    
class ProjectAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email address', max_length=75)
    
    def clean(self):
        username = self.cleaned_data.get('username')
        
        if get_user_model().objects.filter(email__iexact=username, is_regular_user=False).exists():
            raise forms.ValidationError(
                _("This account is not a regular account. Please login with one of our OAuth providers.")
            )

        return super(ProjectAuthenticationForm, self).clean()
    
class ProjectPasswordResetForm(PasswordResetForm):
    
    def save(self, domain_override=None,
             subject_template_name='authentication/password_reset_subject.txt',
             email_template_name='authentication/password_reset_email.html',
             txt_email_template_name='authentication/password_reset_email.txt',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None):
        '''
        Generates a one-use only link for resetting password and sends to the
        user.
        '''
        UserModel = get_user_model()
        email = self.cleaned_data["email"]
        active_users = UserModel._default_manager.filter(
            email__iexact=email, is_active=True)
        for user in active_users:
            # Make sure that no email is sent to a user that actually has
            # a password marked as unusable
            if not user.has_usable_password():
                continue
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            c = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user_id': user.id,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
            }
            
            signals.password_was_reset.send(
                sender=self.__class__,
                context=c
            )
            
            
