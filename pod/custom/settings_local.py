"""Django local settings for pod_project.Django version : 3.2"""

##
# The secret key for your particular Django installation.
#
# This is used to provide cryptographic signing,
# and should be set to a unique, unpredictable value.
#
# Django will not start if this is not set.
# https://docs.djangoproject.com/fr/3.2/ref/settings/#secret-key
#
# SECURITY WARNING: keep the secret key used in production secret!
# You can visit https://djecrety.ir/ to get it 
SECRET_KEY = 'zfrprh&!@mktac#dxp60mv)p6m_h!zxn7icq=5f$i+pt#56iiy'

##
# DEBUG mode activation
#
# https://docs.djangoproject.com/fr/3.2/ref/settings/#debug
#
# SECURITY WARNING: MUST be set to False when deploying into production.
DEBUG = True

##
# A list of strings representing the host/domain names
# that this Django site is allowed to serve.
#
# https://docs.djangoproject.com/fr/3.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['127.0.0.1','localhost']

##
# A tuple that lists people who get code error notifications
#   when DEBUG=False and a view raises an exception.
#
# https://docs.djangoproject.com/fr/3.2/ref/settings/#std:setting-ADMINS
#
ADMINS = (
    ('Benjamin', 'benjamin.sere.etu@univ-lille.fr'),
)


##
# Internationalization and localization.
#
# https://docs.djangoproject.com/fr/3.2/topics/i18n/
# https://github.com/django/django/blob/master/django/conf/global_settings.py
LANGUAGES = (
    ('fr', 'Français'),
    ('en', 'English')
)

#Hide Users in navbar
HIDE_USER_TAB = True
# Hide Types tab in navbar
HIDE_TYPES_TAB = True
# Hide Tags
HIDE_TAGS = True
# Hide disciplines in navbar
HIDE_DISCIPLINES = True

##
# eMail settings
#
# https://docs.djangoproject.com/fr/3.2/ref/settings/#email-host
# https://docs.djangoproject.com/fr/3.2/ref/settings/#email-port
# https://docs.djangoproject.com/fr/3.2/ref/settings/#default-from-email
#
#   username: EMAIL_HOST_USER
#   password: EMAIL_HOST_PASSWORD
#
EMAIL_HOST = 'smtp.univ.fr'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = 'noreply@univ.fr'

# https://docs.djangoproject.com/fr/3.2/ref/settings/#std:setting-SERVER_EMAIL
SERVER_EMAIL = 'noreply@univ.fr'

##
# THIRD PARTY APPS OPTIONNAL
#
USE_PODFILE = True

##
# TEMPLATE Settings
#
TEMPLATE_VISIBLE_SETTINGS = {

    'TITLE_SITE': 'Lille.Pod',
    'TITLE_ETB': 'Université de Lille',
    'LOGO_SITE': 'img/logoPod.svg',
    'LOGO_COMPACT_SITE': 'img/logoPod.svg',
    'LOGO_ETB': 'img/logo_etb.svg',
    'LOGO_PLAYER': 'img/logoPod.svg',
    'FOOTER_TEXT': (
        '42, rue Paul Duez',
        '59000 Lille - France',
        ('<a href="https://goo.gl/maps/AZnyBK4hHaM2"'
            ' target="_blank">Google maps</a>')
    ),
    'LINK_PLAYER': 'http://www.univ-lille.fr',
    'CSS_OVERRIDE': 'custom/mycss.css',
    'PRE_HEADER_TEMPLATE': ''
}

##
# A string representing the time zone for this installation. (default=UTC)
#
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE = 'Europe/Paris'
 
ES_VERSION = 8
ES_URL = ['https://127.0.0.1:9200/'] # ou votre instance déportée
ES_OPTIONS = {'verify_certs' : False, 'basic_auth' : ('pod', 'podpod')}
