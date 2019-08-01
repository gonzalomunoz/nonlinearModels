########################################################################
# launcherSupervisedClf.py,
#
# Exec clf models training
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


from DMA_Kit_Modules.supervised_learning_analysis import execAlgorithm
from DMA_Kit_Modules.utils import responseResults

import pandas as pd
import sys
import argparse

paramsDefault = ["50-SAMME.R", "100-True", "DEFAULT", "gini-best", "DEFAULT","100-deviance-2-1", "5-auto-minkowski-uniform", "relu-adam-constant-1-1-1-0.0001-200-True", "rbf-0.1-3-0.01", "10-gini-2-1-True", "rbf-1-3-0.01"]

#declaracion de los argumentos de entrada
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataSet", help="full path and name to acces dataSet input process", required=True)
parser.add_argument("-o", "--option", type=int, help="Option to Normalize data set: 1. Normal Scale\n2. Min Max Scaler\n3. Log scale\n4. Log normal scale", required=True)
parser.add_argument("-p", "--pathResult", help="full path for save results", required=True)
parser.add_argument("-r", "--responseClass", help="Name of attribute with response class", required=True)
parser.add_argument("-a", "--algorithm", help="Algorithm to process training model: 1. AdaBoostClassifier 2. BaggingClassifier 3. BernoulliNB 4. DecisionTree 5. GaussianNB 6. GradientBoostingClassifier 7. KNeighborsClassifier 8. MLPClassifier 9. NuSVC 10. RandomForest 11. SVC (Default SVC)", required=True)
parser.add_argument("-v", "--validation", help="Cross validation value. If you wont use a Leave One Out, input -1", required=True)
parser.add_argument("-i", "--params", help="Params to exec algorithm, pleas add in this form: param1-param2-param3 for more detail, checks de user manual. If you add Default, it will user the Default params", default="DEFAULT")
parser.add_argument("-u", "--treshold", help="treshold to evaluate encoding features", default="DEFAULT")
args = parser.parse_args()

processData = responseResults.responseProcess()#parser y checks...

if (processData.validatePath(args.pathResult) == 0):

    if (processData.validateDataSetExist(args.dataSet) == 0):

        dataSet = pd.read_csv(args.dataSet)
        option = int(args.option)
        pathResult = args.pathResult
        algorithm = int(args.algorithm)
        validation = int(args.validation)
        featureClass = args.responseClass
        params = args.params
        treshold = args.treshold

        if params == "DEFAULT":
            if algorithm>11 or algorithm<=0:
                algorithm=11
            paramsValues = paramsDefault[algorithm-1]
            paramsValues = paramsValues.split("-")
            print paramsValues
            #hacemos la instancia del obeto...
            execProcess = execAlgorithm.execAlgorithm(dataSet, pathResult, algorithm, paramsValues, validation, featureClass, option, treshold)
            execProcess.execAlgorithmByOptions()#hacemos la ejecucion del algoritmo con respecto a la data que se entrego
        else:
            paramsValues = params.split("-")
            print paramsValues
            #hacemos la instancia del obeto...
            execProcess = execAlgorithm.execAlgorithm(dataSet, pathResult, algorithm, paramsValues, validation, featureClass, option, treshold)
            execProcess.execAlgorithmByOptions()#hacemos la ejecucion del algoritmo con respecto a la data que se entrego
    else:
        print "Data set input not exist, please check the input for name file data set"
else:
    print "Path result not exist, please check input for path result"
