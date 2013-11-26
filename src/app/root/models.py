'''
Created on 21 Oct 2013

@author: michael
'''
from django.db import models

from app.root import constants

class ChoiceModel(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
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

class Application(models.Model):
    # General information
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    area = models.CharField(max_length=255)
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
        choices=constants.INFORMATION_ABOUT_JOZIHUB_CHOICES
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
    events_interesting_in_hosting = models.ManyToManyField(
        EventHostingChoice, 
        blank=True, 
        null=True
    )
    events_interesting_in_hosting_other = models.CharField(
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
        choices=constants.HAPPY_WITH_THE_PRICE_CHOICES
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
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)