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

#http://stackoverflow.com/questions/2801882/generating-a-png-with-matplotlib-when-display-is-undefined
# Force matplotlib to not use any Xwindows backend.
import matplotlib
matplotlib.use('Agg')

from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from piston.resource import Resource
from kluster.clustering.handlers import TagJobHandler

resource = Resource(TagJobHandler)

urlpatterns = patterns('kluster.clustering.views',
   url(r'^pca/$', 'pca_index', name='pca'), 
   url(r'^api/pca/tagjob/(?P<job_id>\d+)/$', resource),
   url(r'^api/pca/tagjob/$', resource),       
)