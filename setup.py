from setuptools import setup, find_packages

setup(
    name='app',
    version='0.0.1',
    url='https://github.com/praekelt/jozihub-web',
    description='Website',
    author='Praekelt Developers',
    author_email='dev@praekeltfoundation.org',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    dependency_links=[
        'http://github.com/unomena/django-photologue/tarball/2.8.praekelt#egg=django-photologue-2.8.praekelt',
        'http://github.com/unomena/django-ckeditor-new/tarball/3.6.2.2#egg=django-ckeditor-3.6.2.2',
        'http://github.com/unomena/tunobase/tarball/1.0.3#egg=tunobase-1.0.3'
    ],
    install_requires=[
        'South',
        'django==1.11.1',
        'django-debug-toolbar==1.8',
        'django-countries',
        'django-polymorphic==1.3',
        'django-ckeditor==3.6.2.2,
        'django-photologue==2.8.praekelt',
        'django-registration==2.3',
        'django-preferences',
        'django-countries==1.5',
        'python-memcached',
        'django_compressor==2.2',
        'gunicorn',
        'celery==4.1',
        'django-celery==3.2.1',
        'django-honeypot',
        'Pillow',
        'psycopg2',
        'flufl.password==1.3',
        'tunobase==1.0.3',
        'raven==6.3',
        'django-extensions'
    ],
    include_package_data=True,
)
