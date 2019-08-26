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

from modulesNLM.clustering_analysis import callService
from modulesNLM.utils import responseResults

import sys
import pandas as pd
import argparse

# def split(dataSet, pathResponse, optionNormalize, featureClass, kindDataSet, threshold, sizeEval):
    # callServiceObject = callService.serviceClustering(dataSet, pathResponse, optionNormalize, featureClass, kindDataSet, threshold, sizeEval)
    # response = callServiceObject.execProcess()
    # print "Dividir G1"
    # print response[0]
    # print "G1"
    # print response[1].shape[0]
    # print "G2"
    # print response[2].shape[0]


class Node(object):
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None
        self.listDataLeft = None
        self.listDataRight = None

class BST(object):
    def __init__(self):
        self.top = None

    def recursBST(self, node, data):            
        if node is None:
            node = Node(data)                
        elif self.top.root > data:
            node.left = self.recursBST(node.left, data)
        elif  self.top.root < data:
            node.right = self.recursBST(node.right, data)
        return node

    # el node es la hoja del arbol, data es el dataset
    def split(self, node, dataSet, pathResponse, optionNormalize, featureClass, kindDataSet, threshold, sizeEval):
        print "Llamando a servicio -> ",dataSet.shape[0]
        callServiceObject = callService.serviceClustering(dataSet, pathResponse, optionNormalize, featureClass, kindDataSet, threshold, sizeEval)
        result = callServiceObject.execProcess()
        if isinstance(result,list):
            if(result[0] == -1):
                print "No puedo dividir: ",dataSet.shape[0]
                return node
            else:
                print "Dividir -> ",dataSet.shape[0]
                listDataLeft = result[1];
                listDataRight = result[2];
                print "G1: ",result[1].shape[0]
                print "G2: ",result[2].shape[0]
                node.left = Node(result[1])
                node.right = Node(result[2])
                node.left = self.split(node.left,result[1], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, sizeEval)
                node.right = self.split(node.right,result[2], pathResponse, optionNormalize, featureClass, kindDataSet, threshold, sizeEval)
        else:
            return 
    def insert(self, data):
        self.top = self.recursBST(self.top, data)
		
    def find(self, val):
        if(self.top != None):
            return self._find(val, self.top)
        else:
            return None

    def _find(self, val, node):
        if(val == node.root):
            return node
        elif(val < node.root and node.left != None):
            self._find(val, node.left)
        elif(val > node.root and node.right != None):
            self._find(val, node.right)

            
            
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
        conv = BST()
        conv.split(conv,dataSet, pathResponse, optionNormalize, featureClass, kindDataSet, threshold, initialSize)
# conv.insert(8)
# conv.insert(3)
# conv.insert(6)
# conv.insert(1)
# conv.insert(-1)
# conv.insert(10)
# conv.insert(14)
# conv.insert(50)
# print (conv.find(3))
