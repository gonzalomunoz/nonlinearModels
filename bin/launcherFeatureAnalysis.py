########################################################################
# launcherFeatureAnalysis.py,
#
# Feature analysis module
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

import sys
import json
import pandas as pd
import argparse

from DMA_Kit_Modules.feature_analysis import execFeatureAnalysis
from DMA_Kit_Modules.utils import responseResults

#recibimos los atributos
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataSet", help="full path and name to acces dataSet input process", required=True)
parser.add_argument("-o", "--option", type=int, help="Option to Normalize data set: 1. Normal Scale\n2. Min Max Scaler\n3. Log scale\n4. Log normal scale", required=True)
parser.add_argument("-p", "--pathResult", help="full path for save results", required=True)
parser.add_argument("-a", "--process", help="Option analyze features: 1.Correlation\n2.Spatial Deformation\n3. PCA\n4. Mutual Information\n5. Kernel PCA\n6. Incremental PCA", required=True)
parser.add_argument("-r", "--attribute", help="Name attribute response in data set", required=False)
parser.add_argument("-k", "--Kind_data", help="Kind of dataSet: 1. CLASS\n2. RESPONSE", required=False)

args = parser.parse_args()

#hacemos las validaciones asociadas a si existe el directorio y el set de datos
processData = responseResults.responseProcess()#parser y checks...

if (processData.validatePath(args.pathResult) == 0):
    if (processData.validateDataSetExist(args.dataSet) == 0):

        dictResponse = {}
        dataSet = pd.read_csv(args.dataSet)
        pathResponse = args.pathResult
        option = int(args.process)
        optionNormalize = int(args.option)

        #instanciamos al objeto
        execFeatures = execFeatureAnalysis.featureAnalysis(dataSet, pathResponse)

        if option != 2:
            if option == 1:#correlation matrix
                dictResponse.update({'Exce': "Correlation Data"})
                response = execFeatures.execCorrelationData(optionNormalize)
                dictResponse.update({"Response": response})
                print dictResponse

            elif option == 3:#PCA
                dictResponse.update({'Exce': "PCA"})
                response = execFeatures.execPCA(optionNormalize)
                dictResponse.update({"Response": response})
                print dictResponse

            elif option == 4:#Mutual Information
                dictResponse.update({'Exce': "Mutual Information"})
                response = execFeatures.execMutualInformation(optionNormalize)
                dictResponse.update({"Response": response})
                print dictResponse

            elif option == 5:#Kernel PCA
                dictResponse.update({'Exce': "Kernel PCA"})
                response = execFeatures.exec_kernelPCA(optionNormalize)
                dictResponse.update({"Response": response})
                print dictResponse
            else:
                dictResponse.update({'Exce': "Incremental PCA"})
                response = execFeatures.execPCA_Incremental(optionNormalize)
                dictResponse.update({"Response": response})
                print dictResponse
            #create file with response...
            with open(pathResponse+"responseProcess.json", 'w') as fp:
                json.dump(dictResponse, fp)

        else:
            if args.Kind_data:
                if args.attribute:
                    if int(args.Kind_data) in [1,2]:
                        dictResponse = {}
                        dataSet = pd.read_csv(args.dataSet)
                        pathResponse = args.pathResult
                        option = int(args.process)
                        optionNormalize = int(args.option)

                        feature = "-"
                        kindDataSet = "-"
                        if int(args.Kind_data) ==1:#class
                            feature = args.attribute
                            kindDataSet = "CLASS"

                        else:#PREDICTION
                            feature = args.attribute
                            kindDataSet = "PREDICTION"
                        dictResponse.update({'Exce': "Spatial Deformation"})
                        response = execFeatures.excecSpatialDeformation(feature, kindDataSet, optionNormalize)
                        dictResponse.update({"Response": response})
                        print dictResponse
                        with open(pathResponse+"responseProcess.json", 'w') as fp:
                            json.dump(dictResponse, fp)
                    else:
                        print "Please select a correct value for kind data set"
                else:
                    print "For this option you most give a value for attribute at response o class"
            else:
                print "For this option you most give a value for kind data set"

    else:
        print "Data set input not exist, please check the input for name file data set"
else:
    print "Path result not exist, please check input for path result"
