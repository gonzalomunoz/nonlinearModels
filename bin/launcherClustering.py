########################################################################
# launcherClustering.py,
#
# Script that allows to execute the clustering which has been selected via web, receives the parameters and generates the pertinent results,
# also works with json format to generate the reading from the javascript on the web side and make the loading of the elements of a
# simplest way
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

from DMA_Kit_Modules.clustering_analysis import execAlgorithm
from DMA_Kit_Modules.checks_module import checksParams
from DMA_Kit_Modules.utils import responseResults

import pandas as pd
import sys
import json
import argparse

#dictParams in defaultCase
paramsDefault = ["3", "3", "ward-euclidean-2", "Default", "Default", "Default"]

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataSet", help="full path and name to acces dataSet input process", required=True)
parser.add_argument("-o", "--option", type=int, help="Option to Normalize data set: 1. Normal Scale\n2. Min Max Scaler\n3. Log scale\n4. Log normal scale", required=True)
parser.add_argument("-p", "--pathResult", help="full path for save results", required=True)
parser.add_argument("-a", "--algorithm", help="Algorithm to process clustering: 1.K-means\n2.Birch\n3.Agglomerative\n4.DBSCAN\n5.MeanShift\n6.Affinity Propagation", required=True)
parser.add_argument("-i", "--params", help="Params to exec algorithm, pleas add in this form: param1-param2-param3")
args = parser.parse_args()

#hacemos las validaciones asociadas a si existe el directorio y el set de datos
processData = responseResults.responseProcess()#parser y checks...

if (processData.validatePath(args.pathResult) == 0):

    if (processData.validateDataSetExist(args.dataSet) == 0):

        dataSet = args.dataSet
        option = int(args.option)
        pathResult = args.pathResult
        algorithm = int(args.algorithm)

        if algorithm >=1:
            if args.params:
                #instanciamos a checksParams para la revision de los parametros
                checksValues = checksParams.checkParams()
                responseData = checksValues.checkParamsCluster(args.params, algorithm)

                if responseData == "OK":
                    #hacemos la ejecucion
                    if algorithm <4:
                        params = args.params.split("-")
                    else:
                        params = args.params
                    #hacemos la instancia del obeto...

                    execProcess = execAlgorithm.execAlgorithm(pd.read_csv(dataSet), pathResult, algorithm, params, option)
                    execProcess.execAlgorithmByOptions()#hacemos la ejecucion del algoritmo con respecto a la data que se entrego
                else:
                    print responseData

            else:
                params = paramsDefault[algorithm-1]

                #hacemos la ejecucion
                if algorithm <4:
                    params = params.split("-")

                #hacemos la instancia del obeto...

                execProcess = execAlgorithm.execAlgorithm(pd.read_csv(dataSet), pathResult, algorithm, params, option)
                execProcess.execAlgorithmByOptions()#hacemos la ejecucion del algoritmo con respecto a la data que se entrego
        else:
            print "Please check input data for select algorithm"
    else:
        print "Data set input not exist, please check the input for name file data set"
else:
    print "Path result not exist, please check input for path result"
