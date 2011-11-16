#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Kluster - A clustering Web Service
#
# Copyright (C) 2011 Thomas Niederberger and individual contributors (see AUTHORS).
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

from mpl_toolkits.mplot3d import Axes3D

from numpy import *
import csv
import logging
import matplotlib.pyplot as plt
import re
import sys

logger = logging.getLogger(__name__)

class Pair:
    count = 1 
    def __init__(self, index):
        self.index = index

class Pca(object):
    #http://de.wikipedia.org/wiki/Hauptkomponentenanalyse
       
    def __init__(self):  
        self.tagLines = []
    
    def pca(self, data, dimensions = 2):
        covariance = cov(transpose(data))
        n = len(covariance)

        # better use svd instead of eig
        val, vec = linalg.eig(covariance)
        eigInd = flipud(argsort(val)[(n-dimensions):n])
        
        # remove means from original data
        noMeansData = data - mean(data, 0)
    
        loc = transpose(dot(transpose(vec[:, eigInd]), transpose(noMeansData)))
        return loc
    
    def generateTagMatrix(self, tagLines, separator=',', minMentions = 3):
        lineCounter = 0
        indexCounter = 0
        tagCounts = {}
        tagMatrix = []
        for line in tagLines:
            line = line.strip()
            tags = re.split('[,]\s*', line)
    
            lineMatrix = []
            for tag in tags:
                if tag not in tagCounts:
                    tagCounts[tag] = Pair(indexCounter)
                    indexCounter += 1
                else:
                    tagCounts[tag].count += 1
                index = tagCounts[tag].index
                lineMatrix.append(index)
            lineCounter += 1
            tagMatrix.append(lineMatrix)
            
        logger.debug(lineCounter)
        relevantIndizes = []
        for tag, pair in tagCounts.iteritems():
            if pair.count >= minMentions:
                logger.debug(tag + " (" + str(pair.index) + "): " + str(pair.count))
                relevantIndizes.append(pair.index)
                
        sciMatrix = zeros((lineCounter, len(relevantIndizes)), int)
        for line in range(lineCounter):
            tagCounter = 0
            for index in relevantIndizes:
                if index in tagMatrix[line]:
                    sciMatrix[line][tagCounter] = 1
                tagCounter += 1
        
        #sciMatrix = np.array(tagMatrix)
        logger.debug(relevantIndizes)
        return sciMatrix;
    
    def add_lines(self, lines):
        self.tagLines.extend(lines)
    
    def load_csv(self, csv_file):
        self.tagLines.extend(open(csv_file, 'r').readlines())
    
    def show(self):
        self._render()
        plt.show()

    def render_file(self, filename):
        self._render()
        plt.savefig(filename)
                
    def _render(self):       
        nDecomp = 2
        tagMatrix = self.generateTagMatrix(self.tagLines, ',', 2)
        
        if len(tagMatrix)>0:
        
            logger.debug(len(tagMatrix[0, :]))
            logger.debug("Records: " + str(len(self.tagLines)))
            
            location = self.pca(tagMatrix, nDecomp)
            
            matchesRecords = sum(tagMatrix, 1)
            matchesTags = sum(tagMatrix, 0)
            correlation = corrcoef(tagMatrix, rowvar=0)
            
            plt.subplot(221)
            plt.title('PCA')
            plt.scatter(real(location[:, 0]), real(location[:, 1]))
            
            plt.subplot(222)
            plt.title('Korrelation')
            plt.imshow(correlation, interpolation='nearest')
            
            plt.subplot(223)
            plt.title('Histogramm Records')
            plt.hist(matchesRecords, range(0, 10))
            
            plt.subplot(224)
            plt.title('Histogramm Tags')
            plt.hist(matchesTags, range(0, max(matchesTags) + 1))