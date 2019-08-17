########################################################################
# LauncherPipeLine.py,
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
import argparse

#inputs: dataset, path output, tipoDataset, FeatureResponse, umbralResponse, percetange minimun for group division, umbral unbalance class

#add params to list
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataSet", help="Full path and name to acces dataSet input process", required=True)
parser.add_argument("-p", "--pathResult", help="Full path for save results", required=True)
parser.add_argument("-m", "--performance", help="Performance selected model", required=True)
parser.add_argument("-k", "--kindDataSet", help="Kind of data set: 1. for classifiers 2. for regression models", required=True)
parser.add_argument("-f", "--feature", help="Name of feature response in dataset", required=True)
parser.add_argument("-u", "--threshold", help="Threshold for umbral response acceptance", required=True)
parser.add_argument("-x", "--percentage", help="Minimun percentage of members in group", required=True)
parser.add_argument("-a", "--proportionClass", help="Minimun porcentage acceptance for unbalance class", required=True)


args = parser.parse_args()
