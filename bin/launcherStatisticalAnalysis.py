########################################################################
# launcherStatisticalAnalysis.py,
#
# Exec statistical analysis option
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


from DMA_Kit_Modules.statistics_analysis import launcherStatisticalData
from DMA_Kit_Modules.utils import responseResults

import sys
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataSet", help="full path and name to acces dataSet input process", required=True)
parser.add_argument("-o", "--option", type=int, help="Option to process: 1. View Continuos Data. 2. Dispersion View. 3. Histogram 4. Frequence. 5. Parallel Coordinates. 6. SPLOM 7. Summary Statistical", required=True)
parser.add_argument("-p", "--pathResult", help="full path for save results", required=True)
parser.add_argument("-a", "--key", help="Key to evaluate in dataSet if you select dispersion or statistical summary, it is not necesarie", default="-")

args = parser.parse_args()

#hacemos las validaciones asociadas a si existe el directorio y el set de datos
processData = responseResults.responseProcess()#parser y checks...

if (processData.validatePath(args.pathResult) == 0):

    if (processData.validateDataSetExist(args.dataSet) == 0):

        dataSet = pd.read_csv(args.dataSet)
        optionProcess = int(args.option)
        pathResponse = args.pathResult
        keyFeature = args.key

        if optionProcess in [1, 3, 4, 5, 6]:
            if keyFeature != "-":
                #instancia al objeto...
                launcherStatisticalDataObject = launcherStatisticalData.launcherStatisticalProcess(dataSet, pathResponse, optionProcess, keyFeature)
                launcherStatisticalDataObject.checkExec()
            else:
                print "You most add a valid number of feature"
        else:
            #instancia al objeto...
            launcherStatisticalDataObject = launcherStatisticalData.launcherStatisticalProcess(dataSet, pathResponse, optionProcess, keyFeature)
            launcherStatisticalDataObject.checkExec()
    else:
        print "Data set input not exist, please check the input for name file data set"
else:
    print "Path result not exist, please check input for path result"
