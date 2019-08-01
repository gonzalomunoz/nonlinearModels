########################################################################
# launcherClusteringScan.py,
#
# Script that allows to run the clustering service,
# input:
#     dataSet
#     job
#     user
#     pathResponse
# response:
#     csv error process
#     csv result process
#     histogram calinski
#     histogram silhouettes
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

from DMA_Kit_Modules.clustering_analysis import callService
from DMA_Kit_Modules.utils import responseResults

import sys
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataSet", help="full path and name to acces dataSet input process", required=True)
parser.add_argument("-o", "--option", type=int, help="Option to Normalize data set: 1. Normal Scale\n2. Min Max Scaler\n3. Log scale\n4. Log normal scale", required=True)
parser.add_argument("-p", "--pathResult", help="full path for save results", required=True)
args = parser.parse_args()

#hacemos las validaciones asociadas a si existe el directorio y el set de datos
processData = responseResults.responseProcess()#parser y checks...

if (processData.validatePath(args.pathResult) == 0):

    if (processData.validateDataSetExist(args.dataSet) == 0):

        #recibimos los datos de entrada...
        dataSet = pd.read_csv(args.dataSet)
        pathResponse = args.pathResult
        optionNormalize = int(args.option)

        #instancia al objeto
        callServiceObject = callService.serviceClustering(dataSet, pathResponse, optionNormalize)
        callServiceObject.execProcess()
    else:
        print "Data set input not exist, please check the input for name file data set"
else:
    print "Path result not exist, please check input for path result"
