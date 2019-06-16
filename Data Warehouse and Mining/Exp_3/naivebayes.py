import pandas as pd
def pci(data):
	classes = [0, 0]
	for i in range(1, len(data)):
		if data.iloc[i, -1] == "Yes":
			classes[0] += 1
		else:
			classes[1] += 1
	return classes[0], classes[1]
def pcix(data, x, pos, neg):
	count_yes= [1 for i in range(len(data.columns) - 1)]
	count_no= [0 for i in range(len(data.columns) - 1)]
	p1,p2 = 1,1
	print(len(data.columns))
	for i in range(len(data)):
		for j in range(len(data.columns)-1):
			if data.iloc[i, j] == x[j]:
				if data.iloc[i, -1] == "Yes":
					count_yes[j] += 1
				else:
					count_no[j] += 1
	for i in range(len(count_no)):
		p1,p2 = p1 * count_yes[i] / pos,p2 * count_no[i] / neg
	return p1, p2
dataset = pd.read_csv('DataSet.csv')
dataset = dataset.iloc[:, 1:]
print(dataset)
X=['Senior','Medium','No','Excellent']
print(X)
c1, c2 = pci(dataset)
p1, p2 = pcix(dataset, X, c1, c2)
print("Yes "+str((p1 * c1)/len(dataset))+" No "+str((p2 * c2) / len(dataset)))
if ((p1 * c1) / len(dataset)) > ((p2 * c2) / len(dataset)):
	print('The person will buy the computer '+str((p1 * c1) / len(dataset)))
else:
	print('The person will not buy the computer '+str((p2 * c2) / len(dataset)))
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM$ python3 naivebayes.py 
       AGE  INCOME STUDENT     CREDIT CLASS
0    Youth    High      No       Fair    No
1    Youth    High      No  Excellent    No
2   Middle    High      No       Fair   Yes
3   Senior  Medium      No       Fair   Yes
4   Senior     Low     Yes       Fair   Yes
5   Senior     Low     Yes  Excellent    No
6   Middle     Low     Yes  Excellent   Yes
7    Youth  Medium      No       Fair    No
8    Youth     Low     Yes       Fair   Yes
9   Senior  Medium     Yes       Fair   Yes
10   Youth  Medium     Yes  Excellent   Yes
11  Middle  Medium      No  Excellent   Yes
12  Middle    High     Yes       Fair   Yes
13  Senior  Medium      No  Excellent    No
['Senior', 'Medium', 'No', 'Excellent']
5
Yes 0.031354105428179506 No 0.05357142857142857
The person will not buy the computer 0.05357142857142857
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM$ 
"""
