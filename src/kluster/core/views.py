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

from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse

def start(request):
    
    methods = [{'url':reverse('pca'),
                'title':'Tags To PCA',
                'text': 'Die Hauptkomponenten Analyse oder englisch Principal Component Analysis (PCA) ist ein Verfahren der multivariaten Statistik.'}]
    
    context = {'title': 'Welcome to Kluster', 'methods':methods*10}
    return TemplateResponse(request, 'start.html', context)
