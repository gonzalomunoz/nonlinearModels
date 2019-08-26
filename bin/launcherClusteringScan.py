########################################################################
# launcherClusteringScan.py,
#
# Script that allows to run the clustering service,
# input:
#     dataSet
#     Option normalize
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
# python launcherClusteringScan.py -d ../dataSetsDemo/vhl/dataCSV.csv -o 1 -p ../dataSetsDemo/vhl/result/ -r Clinical -k 1 -t 10
import matplotlib
matplotlib.use('Agg')
from modulesNLM.clustering_analysis import callService
from modulesNLM.utils import responseResults

import sys
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataSet", help="full path and name to acces dataSet input process", required=True)
parser.add_argument("-o", "--option", type=int, help="Option to Normalize data set: 1. Normal Scale\n2. Min Max Scaler\n3. Log scale\n4. Log normal scale", required=True)
parser.add_argument("-p", "--pathResult", help="full path for save results", required=True)
parser.add_argument("-r", "--response", help="Name response in dataset", required=True)
parser.add_argument("-k", "--kind", type=int, help="Kind of dataset: 1. Classification 2. Regression", required=True)
parser.add_argument("-t", "--threshold", type=int, help="threshold for umbalanced class", required=True)
parser.add_argument("-s", "--initialSize", type=int, help="initial Size of dataset", required=True)

args = parser.parse_args()

#hacemos las validaciones asociadas a si existe el directorio y el set de datos
processData = responseResults.responseProcess()#parser y checks...

if (processData.validatePath(args.pathResult) == 0):

    if (processData.validateDataSetExist(args.dataSet) == 0):

        #recibimos los datos de entrada...
        dataSet = pd.read_csv(args.dataSet)
        pathResponse = args.pathResult
        optionNormalize = int(args.option)
        featureClass = args.response
        kindDataSet = int(args.kind)
        threshold = int(args.threshold)
        # row_count tiene el largo del dataset -1 perteneciente a la de def de columnas
        row_count = sum(1 for line in open(args.dataSet))-1
        print "Size: "
        print row_count
        initialSize = int(args.initialSize)
        initialSize = row_count;
        #instancia al objeto
        callServiceObject = callService.serviceClustering(dataSet, pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
        response = callServiceObject.execProcess()
        print "Dividir G1"
        print response[0]
        print "G1"
        print response[1].shape[0]
        print "G2"
        print response[2].shape[0]
        callServiceObject = callService.serviceClustering(response[1], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
        response1= callServiceObject.execProcess()
        print "Dividir G1_1"
        if(len(response1)>1):
            print response1[0]
            print "G1_1"
            print response1[1].shape[0]
            print "G1_2"
            print response1[2].shape[0]
            callServiceObject = callService.serviceClustering(response1[1], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
            response1_1 = callServiceObject.execProcess()
            print "Dividir G1_1"
            if(isinstance(response1_1,list)==1):
                if(len(response1_1)>1):
                    print response1_1[0]
                    print "G1_1_1"
                    print response1_1[1].shape[0]
                    print "G1_1_2"
                    print response1_1[2].shape[0]				
                    callServiceObject = callService.serviceClustering(response1_1[1], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
                    response1_1_1 = callServiceObject.execProcess()
                    print "G1_1_1"
                    if(isinstance(response1_1_1,list)==1):
                        if(len(response1_1_1)>1):
                            print response1_1_1[0]
                            print "G2_1_1_1_1"
                            print response1_1_1[1].shape[0]
                            print "G2_1_1_1_2"
                            print response1_1_1[2].shape[0]
                    else:
                        print response1_1_1
                        print "No puedo dividir mas"
            callServiceObject = callService.serviceClustering(response1[2], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
            response1_2 = callServiceObject.execProcess()
            if(isinstance(response1_2,list)):
                if(len(response1_2)>1):
                    callServiceObject = callService.serviceClustering(response1_2[1], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
                    response1_2_1 = callServiceObject.execProcess()
                    print "G1_2_1"
                    if(isinstance(response1_2_1,list)):
                        if(len(response1_2_1)>1):
                            print response1_2_1[0]
                            print "G1_1_2_1_1"
                            print response1_2_1[1].shape[0]
                            print "G1_1_2_1_2"
                            print response1_2_1[2].shape[0]
                    else:
                        print "No puedo dividir mas"
        callServiceObject = callService.serviceClustering(response[2], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
        response2= callServiceObject.execProcess()
        print "Dividir G2"
        if(len(response2)>1):
            print response2[0]
            print "G2_1"
            print response2[1].shape[0]
            print "G2_2"
            print response2[2].shape[0]
            callServiceObject = callService.serviceClustering(response2[1], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
            response2_1 = callServiceObject.execProcess()
            print "Dividir G2_1"
            if(isinstance(response2_1,list)==1):
                if(len(response2_1)>1):
                    print response2_1[0]
                    print "G2_1_1"
                    print response2_1[1].shape[0]
                    print "G2_1_2"
                    print response2_1[2].shape[0]
                    callServiceObject = callService.serviceClustering(response2_1[1], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
                    response2_1_1 = callServiceObject.execProcess()
                    print "G2_1_1"
                    if(isinstance(response2_1_1,list)==1):
                        if(len(response2_1_1)>1):
                            print response2_1_1[0]
                            print "G2_1_1_1"
                            print response2_1_1[1].shape[0]
                            print "G2_1_1_2"
                            print response2_1_1[2].shape[0]
                    else:
                        print response2_1_1
                        print "No puedo dividir mas"
            print response2[2].to_csv("data.csv", index=False)
            callServiceObject = callService.serviceClustering(response2[2], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
            response2_2 = callServiceObject.execProcess()
            if(isinstance(response2_2,list)):
                if(len(response2_2)>1):
                    callServiceObject = callService.serviceClustering(response2_2[1], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
                    response2_2_1 = callServiceObject.execProcess()
                    print "G2_2_1"
                    if(isinstance(response2_2_1,list)):
                        if(len(response2_2_1)>1):
                            print response2_2_1[0]
                            print "G2_2_1_1"
                            print response2_2_1[1].shape[0]
                            print "G2_2_1_2"
                            print response2_2_1[2].shape[0]
                    else:
                        print "No puedo dividir mas"
    else:
        print "test Data set input not exist, please check the input for name file data set"
else:
    print "Path result not exist, please check input for path result"
