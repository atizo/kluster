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

from django.core.management.base import BaseCommand, CommandError
from kluster.clustering.pca import Pca

class Command(BaseCommand):
    args = '<csv_file1 csv_file2 ...> <output file>'
    help = 'Generates PCA from CSVs'

    def handle(self, *args, **options):
        pca = Pca()
        
        if len(args) < 2:
            raise CommandError('requires at least 2 arguments')
            
        for csv_file in args[:-1]:
            pca.load_csv(csv_file)
            
        pca.show()
        pca.render_file(args[-1])