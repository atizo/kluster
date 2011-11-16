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

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django_extensions.db.models import TimeStampedModel

DEFAULT = 'png'
FORMAT_CHOICES = (
    (DEFAULT, 'PNG'),
    ('svg', 'SVG'),
    ('pdf', 'PDF'),
    ('ps', 'PS'),
    ('eps', 'EPS'),
)

class TagJob(TimeStampedModel):
    taglines = models.TextField(verbose_name=_(u'Tags'),
                                help_text=_(u'Tags Komma separiert. Jede Entität auf einer neuen Linie'))
    
    format = models.CharField(verbose_name=_(u"Format"),
                              max_length=3,
                              choices=FORMAT_CHOICES, default="")
    
    generated = models.DateTimeField(blank=True, null=True)
    outputfile = models.FileField(upload_to='downloads/', blank=True, null=True)
    
    def get_taglines_list(self):
        return [line for line in self.taglines.replace('\r\n', '\n').replace('\r', '\n').split('\n') if len(line) > 0]
    
    class Meta:
        verbose_name = _(u"Tag Job")
        verbose_name_plural = _(u"Tag Jobs")
        
        
