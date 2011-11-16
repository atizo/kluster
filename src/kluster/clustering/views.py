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
from kluster.clustering.forms import TagForm
from kluster.clustering.handlers import TagJobHandler
from piston.doc import generate_doc
from kluster.core.utils import get_platrom_url

def pca_index(request):
    context = {
               'form': TagForm(), 
               'title': TagJobHandler.name, 
               'domain': get_platrom_url(request), 
               'hanlder_doc': generate_doc(TagJobHandler)
               }
    return TemplateResponse(request, 'pca.html', context)