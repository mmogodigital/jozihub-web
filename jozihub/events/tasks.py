'''
Created on 9 Oct 2015

@author: kaitlyn
'''
from celery.decorators import task

from django.contrib.sites.models import Site
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

from tunobase.mailer import utils as mailer_utils
from app.authentication.models import EndUser

@task(default_retry_delay=10 * 60)
def email_venue_hire(context):
    try:
        admin_emails = (settings.CONTACT_MESSAGE_TO_EMAIL, )
        mailer_utils.send_mail(
            subject='email/subjects/venue_hire_email_subject.txt',
            html_content='email/html/venue_hire_email.html',
            text_content='email/txt/venue_hire_email.txt',
            context=context,
            to_addresses=admin_emails,
        )
    except Exception, exc:
        raise email_venue_hire.retry(exc=exc)
