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

from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^james/', include('djangojames.urls')), 
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('kluster.core.urls')),
    url(r'^clustering/', include('kluster.clustering.urls')),   
)

if settings.DEBUG:
    # Using this method is inefficient and insecure. Do not use this in a production setting. Use this only for development.
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
