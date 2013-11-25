import getpass

APP_NAME = 'app'

REPO_PATH = 'praekelt/jozihub'

PROJECT_NAME = 'jozihub'

IN_HOUSE_DOMAIN = 'unomena.net'

FRONTEND_PROXY_PORT = '12010'

HTTPS_PORT = '443'

PRODUCTION_SERVER_NAME = 'jozihub.com'

DEPLOY_USER = getpass.getuser()

USE_CELERY = True

DEV_SERVERS = ['ubuntu@precise.dev.unomena.net']

QA_SERVERS = ['ubuntu@precise.qa.unomena.net']

PROD_SERVERS = ['ubuntu@web1.prod.unomena.net', 'ubuntu@web2.prod.unomena.net']