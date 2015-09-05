# JoziHub website
## Installation
To get a local development server up and working, do the following:

```
$ virtualenv ve
New python executable in ve/bin/python2.7
Also creating executable in ve/bin/python
Installing setuptools, pip, wheel...done.
$ . ve/bin/activate
(ve)$ ./install.sh
...
Successfully installed South django-debug-toolbar django-countries django-polymorphic django-ckeditor django-photologue django-registration django-preferences python-memcached django-compressor gunicorn celery django-celery django-honeypot Pillow psycopg2 flufl.password tunobase raven app django sqlparse six django-appconf billiard python-dateutil kombu pytz facebook-sdk twython google-api-python-client requests anyjson amqp requests-oauthlib httplib2 oauthlib
Cleaning up...
(ve)$ cd src
(ve)$ ./manage.py syncdb
...

You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): yes
...
> app.jobs
> ckeditor
> photologue
> preferences
> django.contrib.admin
> raven.contrib.django.raven_compat

Not synced (use migrations):
- djcelery
- tunobase.core
- tunobase.mailer
- tunobase.corporate.media
(use ./manage.py migrate to migrate these)
(ve)$ ./manage.py migrate
Running migrations for djcelery:
 - Migrating forwards to 0004_v30_changes.
...
 - Loading initial data for media.
Installed 0 object(s) from 0 fixture(s)
(ve)$ ./manage.py runserver
```
