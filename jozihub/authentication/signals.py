'''
Created on 21 Oct 2013

@author: michael
'''
from django.dispatch import Signal, receiver
from django.conf import settings

# from registration import signals as registration_signals

from jozihub.authentication import tasks

# A contact message has been saved
# password_was_reset = Signal(providing_args=["sender", "context"])


# @receiver(registration_signals.user_registered, weak=False)
# def registration_profile_created(sender, **kwargs):
#     registration_profile = kwargs.pop('registration_profile', None)
#     site = kwargs.pop('site', None)
#     send_email = kwargs.pop('send_email', False)

#     if registration_profile is not None and site is not None and send_email:
#         if settings.USE_CELERY:
#             tasks.email_account_activation.delay(registration_profile.id,
#                                                  site.id)
#         else:
#             tasks.email_account_activation(registration_profile.id, site.id)


# @receiver(registration_signals.user_activated, weak=False)
# def registration_profile_created(sender, **kwargs):
#     activated_user = kwargs.pop('user', None)
#     send_email = kwargs.pop('send_email', False)

#     if activated_user is not None and send_email:
#         if settings.USE_CELERY:
#             tasks.email_account_post_activation.delay(activated_user.id)
#         else:
#             tasks.email_account_post_activation(activated_user.id)


# @receiver(password_was_reset)
# def password_reset(sender, **kwargs):
#     context = kwargs.pop('context', None)

#     if context is not None:
#         if settings.USE_CELERY:
#             tasks.email_password_reset.delay(context)
#         else:
#             tasks.email_password_reset(context)
