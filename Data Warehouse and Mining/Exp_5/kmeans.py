import math
import random
def distance(a, b):
	if type(a) == int or type(a) == float:
		return abs(a - b)
	else:
		return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
def calc_mean(data, dim):
	if dim == 1:
		return sum(data) / len(data)
	else:
		x,y = 0,0
		for i in range(len(data)):
			x += data[i][0]
			y += data[i][1]
		return [x/len(data), y/len(data)]
def kmeans(data, dim, clusters):
	random.shuffle(data)
	means = data[:clusters]
	flag = True
	iteration = 0
	while flag:
		print("Iteration ", iteration)
		print("Means: ", means)
		result = [[] for i in range(clusters)]
		for point in data:
			j,min_dist=0,distance(means[0],point)
			for i in range(1, clusters):
				if distance(means[i], point) < min_dist:
					min_dist = distance(means[i], point)
					j = i
			result[j].append(point)
		print("Clusters: ", result)
		new_means = []
		for cluster in result:
			new_means.append(calc_mean(cluster, dim))
		flag = False
		for i in range(clusters):
			if distance(means[i], new_means[i]) > 0.005:
				flag = True
				means = new_means
				break
		iteration += 1
clusters = int(input('Enter the number of clusters: '))
#data=[2.0, 4.0, 10.0, 12.0, 3.0, 20.0, 30.0, 11.0, 25.0]
#dim=1
data=[[1.0, 1.0], [1.5, 2.0], [3.0, 4.0], [5.0, 7.0], [3.5, 5.0], [4.5, 5.0], [3.5, 4.5]]
dim=2
kmeans(data, dim, clusters)
""" BOTH 1 D AND 2D -AQIDKHATKHATAY
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_5$ python3 kmeans.py 
Enter the number of clusters: 3
Iteration  0
Means:  [20.0, 10.0, 3.0]
Clusters:  [[20.0, 30.0, 25.0], [10.0, 11.0, 12.0], [3.0, 4.0, 2.0]]
Iteration  1
Means:  [25.0, 11.0, 3.0]
Clusters:  [[20.0, 30.0, 25.0], [10.0, 11.0, 12.0], [3.0, 4.0, 2.0]]
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_5$ python3 kmeans.py 
Enter the number of clusters: 2
Iteration  0
Means:  [10.0, 25.0]
Clusters:  [[10.0, 4.0, 12.0, 11.0, 2.0, 3.0], [25.0, 30.0, 20.0]]
Iteration  1
Means:  [7.0, 25.0]
Clusters:  [[10.0, 4.0, 12.0, 11.0, 2.0, 3.0], [25.0, 30.0, 20.0]]
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_5$ python3 kmeans.py 
Enter the number of clusters: 2
Iteration  0
Means:  [[3.5, 5.0], [1.5, 2.0]]
Clusters:  [[[3.5, 5.0], [5.0, 7.0], [4.5, 5.0], [3.0, 4.0], [3.5, 4.5]], [[1.5, 2.0], [1.0, 1.0]]]
Iteration  1
Means:  [[3.9, 5.1], [1.25, 1.5]]
Clusters:  [[[3.5, 5.0], [5.0, 7.0], [4.5, 5.0], [3.0, 4.0], [3.5, 4.5]], [[1.5, 2.0], [1.0, 1.0]]]
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_5$ python3 kmeans.py 
Enter the number of clusters: 3
Iteration  0
Means:  [[3.0, 4.0], [4.5, 5.0], [5.0, 7.0]]
Clusters:  [[[3.0, 4.0], [1.5, 2.0], [1.0, 1.0], [3.5, 4.5]], [[4.5, 5.0], [3.5, 5.0]], [[5.0, 7.0]]]
Iteration  1
Means:  [[2.25, 2.875], [4.0, 5.0], [5.0, 7.0]]
Clusters:  [[[3.0, 4.0], [1.5, 2.0], [1.0, 1.0]], [[4.5, 5.0], [3.5, 5.0], [3.5, 4.5]], [[5.0, 7.0]]]
Iteration  2
Means:  [[1.8333333333333333, 2.3333333333333335], [3.8333333333333335, 4.833333333333333], [5.0, 7.0]]
Clusters:  [[[1.5, 2.0], [1.0, 1.0]], [[3.0, 4.0], [4.5, 5.0], [3.5, 5.0], [3.5, 4.5]], [[5.0, 7.0]]]
Iteration  3
Means:  [[1.25, 1.5], [3.625, 4.625], [5.0, 7.0]]
Clusters:  [[[1.5, 2.0], [1.0, 1.0]], [[3.0, 4.0], [4.5, 5.0], [3.5, 5.0], [3.5, 4.5]], [[5.0, 7.0]]]
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_5$ 
"""
