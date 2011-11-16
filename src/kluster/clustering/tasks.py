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

from kluster.clustering.pca import Pca
import uuid
import os
from django.conf import settings
from celery.decorators import task
from kluster.clustering.models import TagJob
import logging
import datetime

@task
def generate_tagjob(job_id):
    context = {}
    logging.debug('generate_tagjob: %s' % job_id)

    job = TagJob.objects.get(id=job_id)
    
    pca = Pca()
    pca.add_lines(job.get_taglines_list())
    filename = '%s.%s' % (uuid.uuid1(),job.format) 
    filepath = os.path.join(settings.MEDIA_ROOT, 'downloads',filename)
    
    try:     
        pca.render_file(filepath)
        job.outputfile = os.path.join('downloads',filename)
    except:
        logging.exception('could not render output')
    
    job.generated = datetime.datetime.now()
    job.save()
    
    context.update({
        'img': filename,
    })

    return context
