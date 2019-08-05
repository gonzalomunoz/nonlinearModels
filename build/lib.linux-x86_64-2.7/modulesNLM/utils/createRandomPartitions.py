########################################################################
# createRandomPartitions.py,
#
# Copyright (C) 2019  David Medina Ortiz, david.medina@cebib.cl
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
########################################################################

import pandas as pd
import numpy as np
import random

class createRandomDistribution(object):

    def __init__(self, dataSet, n_splitter):

        self.dataSet = dataSet
        self.n_splitter = n_splitter
        self.getKeyAttribute()

    #funcion que permite obtener las listas de las columnas
    def getKeyAttribute(self):

        self.keys = []
        for key in self.dataSet:
            self.keys.append(key)

    #funcion que permite generar numero aleatorios con respecto al tamano del dataset, los numeros no se repiten
    def createRandomValuesDistribution(self):

        self.listIndex = list(range(0, len(self.dataSet)))
        print len(self.dataSet)
        print len(self.listIndex)
        random.shuffle(self.listIndex)

        print self.listIndex
