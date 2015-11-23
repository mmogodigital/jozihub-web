import hashlib
import random
import re
import datetime

from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
try:
    from django.utils.timezone import now as datetime_now
except ImportError:
    datetime_now = datetime.datetime.now

from django_countries.fields import CountryField

from photologue.models import ImageModel

from app.authentication import constants


SHA1_RE = re.compile('^[a-f0-9]{40}$')

class ChoiceModel(models.Model):
    name = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField()
    
    class Meta:
        ordering = ['order']
        abstract = True
    
    def __unicode__(self):
        return u'%s' % self.name

class HeardAboutChoice(ChoiceModel):
    pass
    
class EventHostingChoice(ChoiceModel):
    pass
    
class TypeOfSpaceRequiredChoice(ChoiceModel):
    pass
    
class PartnerChoice(ChoiceModel):
    pass

class EndUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, is_regular_user=True):
        '''
        Creates and saves a User with the given email and password.
        '''
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=EndUserManager.normalize_email(email),
        )
        user.set_password(password)
        user.is_regular_user = is_regular_user
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, password):
        '''
        Creates and saves a superuser with the given email and password.
        '''
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class EndUser(ImageModel, AbstractBaseUser, PermissionsMixin):
    title = models.CharField(max_length=8, choices=constants.TITLE_CHOICES, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=255, blank=True, null=True, unique=True, db_index=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    mobile_number = models.CharField(max_length=16, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    street_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state_province = models.CharField(max_length=255, blank=True, null=True)
    zip_postal_code = models.CharField(max_length=8, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    web_address = models.URLField(blank=True, null=True)
    
    is_regular_user = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_console_user = models.BooleanField(default=False)

    # General Information
    heard_about_from = models.ManyToManyField(
        HeardAboutChoice, 
        blank=True, 
        null=True
    )
    heard_about_from_other = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    affiliation = models.PositiveSmallIntegerField(
        choices=constants.AFFILIATION_CHOICES, 
        blank=True, 
        null=True
    )
    submit_reason = models.PositiveSmallIntegerField(
        choices=constants.SUBMIT_REASON_CHOICES, 
        blank=True, 
        null=True
    )
    information_about_jozihub = models.PositiveSmallIntegerField(
        choices=constants.INFORMATION_ABOUT_JOZIHUB_CHOICES,
        blank=True, 
        null=True
    )

    # About
    educational_background = models.TextField(
        blank=True, 
        null=True
    )
    about_you = models.TextField(
        blank=True, 
        null=True
    )
    events_interested_in_hosting = models.ManyToManyField(
        EventHostingChoice, 
        blank=True, 
        null=True
    )
    events_interested_in_hosting_other = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    when_to_host_event = models.PositiveSmallIntegerField(
        choices=constants.WHEN_TO_HOST_EVENT_CHOICES, 
        blank=True, 
        null=True
    )
    required_from_us = models.TextField(
        blank=True, 
        null=True
    )
    
    # Work space
    how_can_you_contribute_to_jozihub = models.TextField(
        blank=True, 
        null=True
    )
    aims_to_get_from_jozihub = models.TextField(
        blank=True, 
        null=True
    )
    when_to_get_access = models.PositiveSmallIntegerField(
        choices=constants.WHEN_TO_GET_ACCESS_CHOICES, 
        blank=True, 
        null=True
    )
    type_of_space_required = models.ManyToManyField(
        TypeOfSpaceRequiredChoice, 
        blank=True, 
        null=True
    )
    happy_with_the_price = models.PositiveSmallIntegerField(
        choices=constants.HAPPY_WITH_THE_PRICE_CHOICES,
        blank=True, 
        null=True
    )
    
    # Partners
    become_a_partner_or_funder = models.ManyToManyField(
        PartnerChoice, 
        blank=True, 
        null=True
    )
    become_a_partner_or_funder_other = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    about_your_organisation = models.TextField(
        blank=True, 
        null=True
    )
    what_do_you_aim_to_achieve = models.TextField(
        blank=True, 
        null=True
    )
    partnership_expectation = models.TextField(
        blank=True, 
        null=True
    )
    
    # Mentor
    field_of_expertise = models.PositiveSmallIntegerField(
        choices=constants.FIELD_OF_EXPERTISE_CHOICES, 
        blank=True, 
        null=True
    )
    field_of_expertise_other = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    background_and_expertise = models.TextField(
        blank=True, 
        null=True
    )
    what_can_you_offer_as_a_mentor = models.TextField(
        blank=True, 
        null=True
    )
    mentoring_time = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )

    membership_type = models.PositiveSmallIntegerField(
        choices=constants.MEMBERSHIP_TYPE,
        blank=True,
        null=True
    )

    default_image_category = 'user'
    
    USERNAME_FIELD = 'email'
    
    objects = EndUserManager()
    
    def update(self, **kwargs):
        if kwargs.has_key('title'):
            self.title = kwargs['title']
                                         
        if kwargs.has_key('phone'):
            self.phone_number = kwargs['phone']
            
        if kwargs.has_key('mobile'):
            self.mobile_number = kwargs['mobile']

        if kwargs.has_key('password1'):
            self.set_password(kwargs['password1'])
        else:
            self.set_unusable_password()

        self.save()
    
    @property
    def display_name(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        
        return self.get_short_name()
    
    def get_full_name(self):
        # The user is identified by their first name and last name
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        if self.email is not None:
            username = self.email
        else:
            username = self.username
            
        return u'%s' % username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    @property
    def can_access_console(self):
        "Can the user access the console?"
        return any([self.is_console_user, self.is_superuser, self.is_admin])
    
    def save(self, *args, **kwargs):
        from tunobase.core.models import DefaultImage
        
        if not self.image:
            try:
                self.image = DefaultImage.objects.permitted().get_random(self.default_image_category)
            except:
                pass

        return super(EndUser, self).save(*args, **kwargs)

    def mark_deleted(self):
        self.is_active = False
        self.save()

    def get_heard_about_from_options(self):
        return u', '.join([option.name for option in self.heard_about_from.all()])

    def get_events_interested_in_hosting_options(self):
        return u', '.join([option.name for option in self.events_interested_in_hosting.all()])

    def get_become_a_partner_or_funder_options(self):
        return u', '.join([option.name for option in self.become_a_partner_or_funder.all()])

    def get_type_of_space_required_options(self):
        return u', '.join([option.name for option in self.type_of_space_required.all()])

class ProjectRegistrationManager(models.Manager):
    
    def activate_user(self, activation_key):
        """
        Validate an activation key and activate the corresponding
        ``User`` if valid.
        
        If the key is valid and has not expired, return the ``User``
        after activating.
        
        If the key is not valid or has expired, return ``False``.
        
        If the key is valid but the ``User`` is already active,
        return ``False``.
        
        To prevent reactivation of an account which has been
        deactivated by site administrators, the activation key is
        reset to the string constant ``RegistrationProfile.ACTIVATED``
        after successful activation.

        """
        # Make sure the key we're trying conforms to the pattern of a
        # SHA1 hash; if it doesn't, no point trying to look it up in
        # the database.
        if SHA1_RE.search(activation_key):
            try:
                profile = self.get(activation_key=activation_key)
            except self.model.DoesNotExist:
                return False
            if not profile.activation_key_expired():
                user = profile.user
                user.is_active = True
                user.save()
                profile.activation_key = self.model.ACTIVATED
                profile.save()
                return user
        return False
    
    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the address by lowercasing the domain part of the email
        address.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        return email
    
    @transaction.atomic
    def create_inactive_user(self, site, **kwargs):
        email = ProjectRegistrationManager.normalize_email(kwargs['email'])
        for field_name in EndUser._meta.get_all_field_names():
            if not field_name in kwargs:
                kwargs[field_name] = None
        profile = EndUser.objects.create(
            first_name=kwargs['first_name'], 
            last_name=kwargs['last_name'], 
            email=email,
            is_active=False,
            phone_number=kwargs['phone_number'],
            age=kwargs['age'],
            city=kwargs['city'],
            heard_about_from_other=kwargs['heard_about_from_other'],
            affiliation=kwargs['affiliation'],
            submit_reason=kwargs['submit_reason'],
            information_about_jozihub=kwargs['information_about_jozihub'],
            educational_background=kwargs['educational_background'],
            about_you=kwargs['about_you'],
            events_interested_in_hosting_other=kwargs['events_interested_in_hosting_other'],
            when_to_host_event=kwargs['when_to_host_event'],
            required_from_us=kwargs['required_from_us'],
            how_can_you_contribute_to_jozihub=kwargs['how_can_you_contribute_to_jozihub'],
            aims_to_get_from_jozihub=kwargs['aims_to_get_from_jozihub'],
            when_to_get_access=kwargs['when_to_get_access'],
            happy_with_the_price=kwargs['happy_with_the_price'],
            become_a_partner_or_funder_other=kwargs['become_a_partner_or_funder_other'],
            company=kwargs['company'],
            membership_type=kwargs['membership_type'],
            job_title=kwargs['job_title'],
            about_your_organisation=kwargs['about_your_organisation'],
            what_do_you_aim_to_achieve=kwargs['what_do_you_aim_to_achieve'],
            partnership_expectation=kwargs['partnership_expectation'],
            field_of_expertise=kwargs['field_of_expertise'],
            field_of_expertise_other=kwargs['field_of_expertise_other'],
            background_and_expertise=kwargs['background_and_expertise'],
            what_can_you_offer_as_a_mentor=kwargs['what_can_you_offer_as_a_mentor'],
            mentoring_time=kwargs['mentoring_time'],
        )
        if kwargs['heard_about_from']:
            profile.heard_about_from.add(kwargs['heard_about_from'])

        if kwargs['become_a_partner_or_funder']:
            profile.become_a_partner_or_funder.add(kwargs['become_a_partner_or_funder'])

        if kwargs['type_of_space_required']:
            profile.type_of_space_required.add(kwargs['type_of_space_required'])

        if kwargs['events_interested_in_hosting']:
            profile.events_interested_in_hosting.add(kwargs['events_interested_in_hosting'])

        profile.update(**kwargs)

        registration_profile = self.create_profile(profile)

        return registration_profile
    
    @transaction.atomic
    def create_active_user(self, site, **kwargs):
        email = ProjectRegistrationManager.normalize_email(kwargs['email'])
        for field_name in EndUser._meta.get_all_field_names():
            if not field_name in kwargs:
                kwargs[field_name] = None
        profile = EndUser.objects.create(
            first_name=kwargs['first_name'], 
            last_name=kwargs['last_name'], 
            email=email,
            is_active=True,
            phone_number=kwargs['phone_number'],
            age=kwargs['age'],
            city=kwargs['city'],
            heard_about_from_other=kwargs['heard_about_from_other'],
            affiliation=kwargs['affiliation'],
            submit_reason=kwargs['submit_reason'],
            information_about_jozihub=kwargs['information_about_jozihub'],
            educational_background=kwargs['educational_background'],
            about_you=kwargs['about_you'],
            events_interested_in_hosting_other=kwargs['events_interested_in_hosting_other'],
            when_to_host_event=kwargs['when_to_host_event'],
            required_from_us=kwargs['required_from_us'],
            how_can_you_contribute_to_jozihub=kwargs['how_can_you_contribute_to_jozihub'],
            aims_to_get_from_jozihub=kwargs['aims_to_get_from_jozihub'],
            when_to_get_access=kwargs['when_to_get_access'],
            happy_with_the_price=kwargs['happy_with_the_price'],
            become_a_partner_or_funder_other=kwargs['become_a_partner_or_funder_other'],
            about_your_organisation=kwargs['about_your_organisation'],
            company=kwargs['company'],
            membership_type=kwargs['membership_type'],
            job_title=kwargs['job_title'],
            what_do_you_aim_to_achieve=kwargs['what_do_you_aim_to_achieve'],
            partnership_expectation=kwargs['partnership_expectation'],
            field_of_expertise=kwargs['field_of_expertise'],
            field_of_expertise_other=kwargs['field_of_expertise_other'],
            background_and_expertise=kwargs['background_and_expertise'],
            what_can_you_offer_as_a_mentor=kwargs['what_can_you_offer_as_a_mentor'],
            mentoring_time=kwargs['mentoring_time'],
        )
        if kwargs['heard_about_from']:
            profile.heard_about_from.add(kwargs['heard_about_from'])

        if kwargs['become_a_partner_or_funder']:
            profile.become_a_partner_or_funder.add(kwargs['become_a_partner_or_funder'])

        if kwargs['type_of_space_required']:
            profile.type_of_space_required.add(kwargs['type_of_space_required'])

        if kwargs['events_interested_in_hosting']:
            profile.events_interested_in_hosting.add(kwargs['events_interested_in_hosting'])

        profile.update(**kwargs)

        return profile
    
    def create_profile(self, user):
        """
        Create a ``RegistrationProfile`` for a given
        ``User``, and return the ``RegistrationProfile``.
        
        The activation key for the ``RegistrationProfile`` will be a
        SHA1 hash, generated from a combination of the ``User``'s
        username and a random salt.
        
        """
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        username = user.get_username()
        if isinstance(username, unicode):
            username = username.encode('utf-8')
        activation_key = hashlib.sha1(salt+username).hexdigest()
        
        return self.create(user=user, activation_key=activation_key)
    
    def delete_expired_users(self):
        """
        Remove expired instances of ``RegistrationProfile`` and their
        associated ``User``s.
        
        Accounts to be deleted are identified by searching for
        instances of ``RegistrationProfile`` with expired activation
        keys, and then checking to see if their associated ``User``
        instances have the field ``is_active`` set to ``False``; any
        ``User`` who is both inactive and has an expired activation
        key will be deleted.
        
        It is recommended that this method be executed regularly as
        part of your routine site maintenance; this application
        provides a custom management command which will call this
        method, accessible as ``manage.py cleanupregistration``.
        
        Regularly clearing out accounts which have never been
        activated serves two useful purposes:
        
        1. It alleviates the ocasional need to reset a
           ``RegistrationProfile`` and/or re-send an activation email
           when a user does not receive or does not act upon the
           initial activation email; since the account will be
           deleted, the user will be able to simply re-register and
           receive a new activation key.
        
        2. It prevents the possibility of a malicious user registering
           one or more accounts and never activating them (thus
           denying the use of those usernames to anyone else); since
           those accounts will be deleted, the usernames will become
           available for use again.
        
        If you have a troublesome ``User`` and wish to disable their
        account while keeping it in the database, simply delete the
        associated ``RegistrationProfile``; an inactive ``User`` which
        does not have an associated ``RegistrationProfile`` will not
        be deleted.
        
        """
        for profile in self.all():
            try:
                if profile.activation_key_expired():
                    user = profile.user
                    if not user.is_active:
                        user.delete()
                        profile.delete()
            except EndUser.DoesNotExist:
                profile.delete()
    
class ProjectRegistrationProfile(models.Model):
    ACTIVATED = u"ALREADY_ACTIVATED"
    
    user = models.ForeignKey(EndUser, unique=True, verbose_name=_('user'))
    activation_key = models.CharField(_('activation key'), max_length=40)
    
    objects = ProjectRegistrationManager()
    
    class Meta:
        verbose_name = _('registration profile')
        verbose_name_plural = _('registration profiles')
    
    def __unicode__(self):
        return u"Registration information for %s" % self.user
    
    def activation_key_expired(self):
        """
        Determine whether this ``RegistrationProfile``'s activation
        key has expired, returning a boolean -- ``True`` if the key
        has expired.
        
        Key expiration is determined by a two-step process:
        
        1. If the user has already activated, the key will have been
           reset to the string constant ``ACTIVATED``. Re-activating
           is not permitted, and so this method returns ``True`` in
           this case.

        2. Otherwise, the date the user signed up is incremented by
           the number of days specified in the setting
           ``ACCOUNT_ACTIVATION_DAYS`` (which should be the number of
           days after signup during which a user is allowed to
           activate their account); if the result is less than or
           equal to the current date, the key has expired and this
           method returns ``True``.
        
        """
        expiration_date = datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
        return self.activation_key == self.ACTIVATED or \
               (self.user.date_joined + expiration_date <= datetime_now())
    activation_key_expired.boolean = True
