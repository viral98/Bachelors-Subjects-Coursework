import numpy as np
import pandas as pd
import pprint
from numpy import log2 as log

eps = np.finfo(float).eps
def findDatasetEntropy(dataset):
	entropy=0
	uniqueValues = dataset.CLASS.unique()
	for value in uniqueValues:
		fraction = dataset.CLASS.value_counts()[value]/len(dataset.CLASS)
		entropy += -fraction*log(fraction)
	return abs(entropy)

def findAttributeEntropy(dataset,attribute):
	entropy=0
	attributeEntropy=0
	targetVariables = dataset.CLASS.unique()
	variables =dataset[attribute].unique()

	for variable in variables:
		featureEntropy=0

		for targetVariable in targetVariables:
			num = len(dataset[attribute][dataset[attribute]==variable][dataset.CLASS==targetVariable])
			den = len(dataset[attribute][dataset[attribute]==variable])
			fraction = num/(den+eps)
			featureEntropy += -fraction*log(fraction+eps)

		entropy += (den/len(dataset))*featureEntropy

	return abs(entropy)

def maxInformationGain(dataset,attributes,datasetEntropy):
	attributeEntropy={}
	informationGain={}

	for attribute in attributes:
		attributeEntropy[attribute] = findAttributeEntropy(dataset,attribute)
		informationGain[attribute] = datasetEntropy - attributeEntropy[attribute]

	maximum=0
	ki = attribute

	for key,value in informationGain.items():
		if value > maximum:
			maximum = value
			ki = key
			print(key,value)

	print("Split on",ki)
	return ki

def getSubDataset(dataset,keyNode,attribute):
	return dataset[dataset[keyNode]==attribute].reset_index(drop=True)

def buildTree(dataset,tree=None):
	datasetEntropy = findDatasetEntropy(dataset)
	attr = dataset.keys()[:-1]

	key = maxInformationGain(dataset,attr,datasetEntropy)
	attributes = np.unique(dataset[key])

	if tree is None:
		tree={}
		tree[key]={}
	
	for attribute in attributes:
		subtable = getSubDataset(dataset,key,attribute)
		classvals,count = np.unique(subtable['CLASS'],return_counts=True)

		if len(count)==1:
			tree[key][attribute] = classvals[0]
		else:
			tree[key][attribute] = buildTree(subtable)

	return tree

dataset = pd.read_csv('decisiontree.csv')
dataset = dataset.iloc[:,1:]
tree = buildTree(dataset)
pprint.pprint(tree)