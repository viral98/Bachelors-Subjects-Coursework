import math
class Node:
    def __init__(self, name):
        self.name = name
        self.label =self.decisionAttr=self.decisionGain=self.decisionValue= None
        self.branches = []
    def printTree(self):
        self.printTreeRecurse(0)
    def printTreeRecurse(self, level):
        print ('\t' * level + self.name)
        if self.decisionAttr and self.decisionGain:
            print('split by ' + str(self.decisionAttr) + ' for a gain of ' + str(self.decisionGain))
        if self.label:
            print(' ' + self.label)
        level += 1
        for branch in self.branches:
            branch.printTreeRecurse(level)
    def predictOutcome(self, cases, a):
        predictions = []
        for c in cases:
            predictions.append(self.predictOutcomeRecurse(c, attributes))
        return predictions
    def predictOutcomeRecurse(self, case, a):
        if self.name == '':
            if self.label == 'Yes':
                return 'Yes'
            elif self.label == 'No':
                return 'No'
        index = a.index(self.decisionAttr)
        if self.decisionValue == case[index]:
            return self.branches[0].predictOutcomeRecurse(case, a)
        if self.decisionGain:
            for b in self.branches:
                if b.decisionValue == case[index]:
                    return b.predictOutcomeRecurse(case, a)
def constructDecisionTree(rows, targetAttribute, attributes):
    root = Node('')
    if all(isPositive(row[-1]) for row in rows):
        root.label = 'Yes'
        return root
    elif all(not isPositive(row[-1]) for row in rows):
        root.label = 'No'
        return root
    else:
        result = getHighestInfoGainAttr(attributes, rows)
        attr,gain,attrIndex = result[0],result[1],result[2]
        root.decisionAttr,root.decisionGain = attr,gain
        possibleValues = uniqueValues(attrIndex, rows)
        for value in possibleValues:
            newBranch = Node(attr + ' = ' + value)
            newBranch.decisionAttr = attr
            newBranch.decisionValue = value
            root.branches.append(newBranch)
            branchRows = sorted(row for row in rows if row[attrIndex] == value)
            if not branchRows:
                leaf = Node(getMostCommonValue(targetAttribute, rows, possibleValues))
                newBranch.branches.append(leaf)
            else:
                newRows = []
                for row in branchRows:
                    newRow = []
                    for i in range(len(row)):
                        if not i == attrIndex:
                            newRow.append(row[i])
                    newRows.append(newRow)
                newBranch.branches.append(constructDecisionTree(newRows, targetAttribute, [a for a in attributes if not a == attr]))
    return root
def isPositive(word):
    word = word.lower()
    return word == 'yes' or word == 'true' or word == 'y' or word == 't'
def getMostCommonLabel(nodes):
    pCount,nCount = 0,0
    for node in nodes:
        if node.label == 'Yes':
            pCount += 1
        elif node.label == 'No':
            nCount += 1
    if pCount >= nCount:
        return 'Yes'
    else:
        return 'No'
def getHighestInfoGainAttr(attributes, rows):
    totalRows = len(rows)
    posrows = sorted(row for row in rows if isPositive(row[-1]))
    negrows = sorted(row for row in rows if not isPositive(row[-1]))
    allExpectedInfo = computeExpectedInfo(len(posrows), len(negrows))
    valuesGain = []
    for i, attr in enumerate(attributes):
        if attributes[-1] == attributes[i]:
            break
        values = uniqueValues(i, rows)
        valuesExpectedInfo,valuesProbability = [],[]
        for value in values:
            posRowsOfValue = sorted(row for row in posrows if row[i]==value)
            negRowsOfValue = sorted(row for row in negrows if row[i]==value)
            numPos,numNeg = len(posRowsOfValue),len(negRowsOfValue)
            valueExpectedInfo = computeExpectedInfo(numPos, numNeg)
            valueProbability = float(numPos + numNeg) / float(totalRows)
            valuesExpectedInfo.append(valueExpectedInfo)
            valuesProbability.append(valueProbability)
        valueEntropy = computeEntropy(valuesExpectedInfo, valuesProbability)
        valueGain = allExpectedInfo - valueEntropy
        valuesGain.append(valueGain)
    index = valuesGain.index(max(valuesGain))
    return [attributes[index], valuesGain[index], index]
def computeExpectedInfo(count1, count2):
    count1,count2 = float(count1),float(count2)
    total = count1 + count2
    prob1,prob2 = count1/total,count2/total
    if prob1 > 0.0 and prob2 > 0.0:
        return -prob1 * math.log(prob1, 2.0) - prob2 * math.log(prob2, 2.0)
    elif prob1 > 0.0:
        return -prob1 * math.log(prob1, 2.0)
    elif prob2 > 0.0:
        return -prob2 * math.log(prob2, 2.0)
    return	
def computeEntropy(p, e):
    entropy = 0.0
    for i in range(len(p)):
        entropy += p[i] * e[i]
    return entropy
def uniqueValues(attrIndex, rows):
    values = []
    for r in rows:
        if r[attrIndex] not in values:
            values.append(r[attrIndex])
    return values
def getMostCommonValue(attr, rows, values):
    valueCounts = []
    for value in values:
        valueCount = 0
        for row in rows:
            if row[attr] == value:
                valueCount += 1
        valueCounts.append(valueCount)
    return values[valueCounts.index(max(valueCounts))]
def constructTreeFromFile(f_train,attributes):
    rows = []
    for line in f_train:
        rows.append([item.strip() for item in line.split(',')])
    return constructDecisionTree(rows, attributes[-1], attributes)
f_train,f_test = open("train", 'r'),open("test",'r')
attrLine = f_train.readline()
attributes =[a.strip() for a in attrLine.split(',')]
tree = constructTreeFromFile(f_train,attributes)
tree.printTree()
cases=[]
for line in f_test:
	case = [item.strip() for item in line.split(',')]
	cases.append(case)
print (tree.predictOutcome(cases,attributes.pop(-1)))
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_3$ python3 decision_tree.py 

split by AGE for a gain of 0.2467498197744391
	AGE = Youth
		
split by STUDENT for a gain of 0.9709505944546686
			STUDENT = No
				
 No
			STUDENT = Yes
				
 Yes
	AGE = Middle
		
 Yes
	AGE = Senior
		
split by CREDIT for a gain of 0.9709505944546686
			CREDIT = Excellent
				
 No
			CREDIT = Fair
				
 Yes
['Yes']
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_3$ 
"""
