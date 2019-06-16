import math
import random

def distance(a,b):
	if((type(a)==int or type (a)==float) and (type(b)==int or type(b)==float)):
		return abs(a-b)
	else:
		return abs((a[0]-b[0])**2+(a[1]-b[1])**2)

def calculateMean(data,dim):
	if dim==1:
		return abs(sum(data)/len(data))
	else:
		x,y=0,0
		for i in range(len(data)):
			x+=data[i][0]
			y+=data[0][i]
			return [abs(x/len(data),y/len(data))]


def kmeans(data,dim,clusters):
	random.shuffle(data)
	means = data[:clusters]
	iteration = 0
	flag = True
	iteration=0
	
	while flag:
		result = [[] for i in range(clusters) ]
		for point in data:
			j,minimumDistance = 0,means[0]
			for i in range(clusters):
				if distance(means[i],point)<minimumDistance:
					minimumDistance = distance(means[i],point)
					j=i
			result[j].append(point)
		print("Clusters: ", result)
		new_mean = []

		for j in result:
			new_mean.append(calculateMean(j,dim))

		flag=False

		for i in range(clusters):
			if(distance(new_mean[i],means[i])>0.005):
				flag=True
				means=new_mean
				break

		iteration+=1

clusters = int(input('Enter the number of clusters: '))
data=[2.0, 4.0, 10.0, 12.0, 3.0, 20.0, 30.0, 11.0, 25.0]
dim=1
# data=[[1.0, 1.0], [1.5, 2.0], [3.0, 4.0], [5.0, 7.0], [3.5, 5.0], [4.5, 5.0], [3.5, 4.5]]
# dim=2
kmeans(data, dim, clusters)