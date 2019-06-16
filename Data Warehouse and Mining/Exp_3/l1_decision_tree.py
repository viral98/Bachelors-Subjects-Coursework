import math
def entropy(dataset):
    total = 0.0
    labels = [row[-1] for row in dataset]
    n = len(labels)
    for label in list(set(labels)):
        p = labels.count(label) / n
        if p != 0:
            total += p * math.log(1/p, 2)
    return total
def split(dataset,  feature):
    values = list(set([row[feature] for row in dataset]))
    children = []
    for i in range(len(values)):
        children.append([])
        for row in dataset:
            if row[feature] == values[i]:
                children[i].append(row)
    return children
def information(dataset, feature):
    info = 0.0
    children = split(dataset, feature)
    n = sum([len(child) for child in children])
    for child in children:
        info += (len(child) / n) * entropy(child)
    return info
def select_best_feature(dataset, attributes):
    info = 999
    feature = 999
    for i in range(len(dataset[0]) - 1):
        temp = information(dataset, i)
        print('Information for feature', attributes[i], ':', temp)
        if temp < info:
            info = temp
            feature = i
    return feature
data=[['Youth', 'High', 'No', 'Fair', 'No'],
 ['Youth', 'High', 'No', 'Excellent', 'No'],
 ['Middle', 'High', 'No', 'Fair', 'Yes'],
 ['Senior', 'Medium', 'No', 'Fair', 'Yes'],
 ['Senior', 'Low', 'Yes', 'Fair', 'Yes'],
 ['Senior', 'Low', 'Yes', 'Excellent', 'No'],
 ['Middle', 'Low', 'Yes', 'Excellent', 'Yes'],
 ['Youth', 'Medium', 'No', 'Fair', 'No'],
 ['Youth', 'Low', 'Yes', 'Fair', 'Yes'],
 ['Senior', 'Medium', 'Yes', 'Fair', 'Yes'],
 ['Youth', 'Medium', 'Yes', 'Excellent', 'Yes'],
 ['Middle', 'Medium', 'No', 'Excellent', 'Yes'],
 ['Middle', 'High', 'Yes', 'Fair', 'Yes'],
 ['Senior', 'Medium', 'No', 'Excellent', 'No']]
attributes={ 0: 'AGE', 1: 'INCOME', 2: 'STUDENT', 3: 'CREDIT'}
f = select_best_feature(data, attributes)
attr=attributes[f]
print('The feature  with least entropy and largest gain is', attr)   
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_3$ python3 l1_decision_tree.py 
Information for feature AGE : 0.6935361388961919
Information for feature INCOME : 0.9110633930116762
Information for feature STUDENT : 0.7884504573082894
Information for feature CREDIT : 0.8921589282623614
The feature  with least entropy and largest gain is AGE
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_3$ 
"""
