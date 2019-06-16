import pandas as pd
def pci(data):
	classes = [0,0]
	for i in range(1,len(data)):
		if data.iloc[i,-1] == 'Yes':
			classes[0]+=1
		else:
			classes[1]+=1
	return classes[0],classes[1]
def pcix(data,x,pos,neg):
	class_yes = [1 for i in range(len(data.columns)-1)]
	class_no = [0 for i in range(len(data.columns)-1)]
	p1,p2 = 1,1
	print(len(data.columns))
	for i in range(len(data)):
		for j in range(len(data.columns)-1):
			if data.iloc[i, j] == x[j]:
				if data.iloc[i,-1]=='Yes':
					class_yes[j]+=1
				else:
					class_no[j]+=1

	for i in range(len(class_no)):
		p1 = p1 * class_yes[i]/pos
		p2 = p2 * class_no[i]/neg

	return p1,p2

data = pd.read_csv('DataSet.csv')
data = data.iloc[:, 1:]
X=['Senior','Medium','No','Excellent']
pos,neg=pci(data)
p1,p2=pcix(data,X,pos,neg)

if ((p1 * pos) / len(data)) > ((p2 * neg) / len(data)):
	print('The person will buy the computer '+str((p1 * pos) / len(data)))
else:
	print('The person will not buy the computer '+str((p2 * neg) / len(data)))

