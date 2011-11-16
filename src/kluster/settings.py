#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Kluster - A clustering Web Service
#
# Copyright (C) 2011 Atizo AG and individual contributors (see AUTHORS).
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os

try:
    from settings_local import *
except ImportError:
    pass

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

ugettext = lambda s: s

MANAGERS = ADMINS

PISTON_DISPLAY_ERRORS = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
                    os.path.join(PROJECT_ROOT, '../../../kluster-env/lib/python2.6/site-packages/admin_tools/media/'),
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'
ADMIN_TOOLS_THEMING_CSS = 'css/admin-theming.css'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#4&@i60593n_d+q-rq49nrt6^@*^tsn62=1e$2md(zxwsw#6s8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',    
)

ROOT_URLCONF = 'kluster.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',                  
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'django_extensions',
    'djangojames',
    'djcelery',
    'piston',
    'kluster.core',
    'kluster.clustering',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'external_fixtures/'),
)

ADMIN_TOOLS_THEMING_CSS = 'djangojames/css/admin_theming.css'
ADMIN_TOOLS_INDEX_DASHBOARD = 'djangojames.admin_dashboard.CustomIndexDashboard'

if USE_DEBUG_TOOLBAR:
    
    INSTALLED_APPS += ('debug_toolbar',)
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.sql.SQLDebugPanel',
        #'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',        
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )    
    DEBUG_TOOLBAR_URL_EXCLUDE = (
        '/site_media/{% extends "base.html" %}1/',        
    )    
    
    DEBUG_TOOLBAR_CONFIG = {
     'INTERCEPT_REDIRECTS': False,  # Setting to True will intercept redirects. (True)
     'LOGGING_ENABLED': False,     # Enable logging. (True)                       
     }
        
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    
APPEND_SLASH = True