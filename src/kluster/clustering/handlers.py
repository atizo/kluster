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

from piston.handler import BaseHandler
from piston.utils import rc, throttle
from kluster.clustering.models import TagJob
from piston.utils import validate
from kluster.clustering.forms import TagForm
from kluster.clustering.tasks import generate_tagjob
from django.conf import settings
import urlparse

import logging
from kluster.core.utils import get_platrom_url
logger = logging.getLogger(__name__)

class TagJobHandler(BaseHandler):
    """bq. Die Hauptkomponentenanalyse oder englisch Principal Component Analysis (PCA) \
ist ein Verfahren der multivariaten Statistik. Sie dient dazu, umfangreiche Datensätze \
zu strukturieren, zu vereinfachen und zu veranschaulichen, indem eine Vielzahl statistischer \
Variablen durch eine geringere Zahl möglichst aussagekräftiger Linearkombinationen \
(die „Hauptkomponenten“) genähert wird. Speziell in der Bildverarbeitung wird die \
Hauptkomponentenanalyse auch Karhunen-Loève-Transformation genannt. 
Sie ist von der Faktorenanalyse zu unterscheiden, mit der sie formale Ähnlichkeit hat \
und in der sie als Näherungsmethode zur Faktorenextraktion verwendet werden kann.
(Aus der "Wikipedia":http://de.wikipedia.org/wiki/Hauptkomponentenanalyse)
       
Abfragen können mit "Representational state transfer (REST)":http://en.wikipedia.org/wiki/Representational_state_transfer gemacht werden. \
    """
    name = 'Tag To Pca'
    allowed_methods = ('GET', 'POST',  'DELETE') 
    fields = ('id','generated', 'format', 'outputfile_url', 'created', 'done')
    model = TagJob

    @classmethod
    def done(self, tagjob):
        if tagjob.generated:
            return True
        else:
            return False

    @classmethod
    def outputfile_url(self, tagjob):
        if self.done(tagjob) and tagjob.outputfile:
            return urlparse.urljoin('http://%s' % get_platrom_url(), tagjob.outputfile.url)
        return None
        
    def read(self, request, job_id=None):
        """
GET: Zugriff auf eine 'Tag To Pca' Abfrage
Wird keine Job id angegeben werden alle 'Tag To Pca' Abfragen zurück gegeben
    
Javascript Example:
    
pre. $.ajax({
    url: 'http://kti.atizo.org/clustering/api/pca/tagjob/1/,
    type: 'GET',
    success: function(data) {
            ...
        } 
    }
});
        """
        query = TagJob.objects
        if job_id:
            try:
                job = query.get(id=job_id)
            except TagJob.DoesNotExist:
                return rc.NOT_FOUND
        else:
            return query.all()
            
        return job
    
    @validate(TagForm, 'POST')
    def create(self, request):
        """
POST: Neue 'Tag To Pca' Abfrage anlegen

Javascript Example:

pre. $.ajax({
    url: 'http://kti.atizo.org/clustering/api/pca/tagjob/,
    type: 'POST',
    data: {format: 'png', taglines: ... },
    success: function(data) {
           ...
        } 
    }
});
       
        """
        job = request.form.save()
        generate_tagjob.delay(job.id)
        return job
        
    def delete(self, request, job_id):
        """
DELETE: 'Tag To Pca' Abfrage löschen

Javascript Example:

pre. $.ajax({
    url: 'http://kti.atizo.org/clustering/api/pca/tagjob/1,
    type: 'DELETE'
});     
        """
        try:
            job = TagJob.objects.get(id=job_id)
            job.delete()
        except TagJob.DoesNotExist:
            return rc.NOT_FOUND
        
        return rc.DELETED
