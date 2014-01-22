import getpass

# Don't change this. Leave as 'app'
APP_NAME = 'app'

REPO_PATH = 'praekelt/jozihub'

PROJECT_NAME = 'jozihub'

IN_HOUSE_DOMAIN = 'unomena.net'

FRONTEND_PROXY_PORT = '12010'

HTTPS_PORT = '443'

PRODUCTION_SERVER_NAME = 'jozihub.com'

PRODUCTION_SERVER_NAMES = 'jozihub.com'

DEPLOY_USER = getpass.getuser()

USE_CELERY = True

CONFIGURE_SETTINGS_LOCAL = True

DB_TO_CONFIGURE = 'postgres'
#DB_TO_CONFIGURE = 'mysql'

CONFIGURE_DB = True

SYNC_DB = CONFIGURE_DB

CONFIGURE_RABBITMQ = True

WEBSERVER_TO_CONFIGURE = 'nginx'
#WEBSERVER_TO_CONFIGURE = 'apache'

CONFIGURE_SUPERVISOR = True

CONFIGURE_CERT = True

RUN_MIGRATIONS = True

RUN_TESTS = True

DEV_SERVERS = ['ubuntu@precise.dev.unomena.net']

QA_SERVERS = ['ubuntu@precise.qa.unomena.net']

PROD_SERVERS = ['ubuntu@web1.prod.unomena.net', 'ubuntu@web2.prod.unomena.net']

TESTS_TO_RUN = (
    'app.authentication '
    'tunobase.core '
    'tunobase.blog '
    'tunobase.commenting '
    'tunobase.poll '
    'tunobase.social_media.tunosocial'
)
