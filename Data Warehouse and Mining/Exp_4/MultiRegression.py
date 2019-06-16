def linearRegression(x, y, num_features):
	n = len(y)
	theta = [0 for i in range(num_features + 1)]
	alpha = 0.00001 
	for iteration in range(400):
		new = []
		h = [predict(sample, theta) for sample in x]
		diff = [(h[i]-y[i]) for i in range(n)]
		for i in range(num_features + 1):
			temp = 0
			for j in range(n):
				temp += diff[j]*x[j][i]
			new.append(theta[i] - (alpha/n)*temp)
		theta = new[:]
	return theta
def predict(sample, theta):
	y = 0
	for i in range(len(sample)):
		y += sample[i]*theta[i]
	return y
def accuracy(test_x, test_y, theta):
	acc = 0
	for i in range(len(test_x)):
		if abs(predict(test_x[i], theta) - test_y[i]) < 10:  
			acc += 1
	return acc/len(test_x)
x=[[1.0,2.0,165.0], [1.5,2.0,170.0], [1.7,2.0,175.0], [3.0,3.0,180.0], [5.0,4.0,185.0], [4.0,5.0,190.0], [2.0,5.3,195.0]]
y= [38.0, 39.0, 42.0, 44.5, 43.0, 45.0, 46.0]
num_features = 2
n = len(x)
train_x, train_y = x[:(2*n)//3], y[:(2*n)//3]
test_x, test_y = x[(2*n)//3:], y[(2*n)//3:]
theta = linearRegression(train_x, train_y, num_features)
print(theta)
print("Accuracy:", accuracy(test_x, test_y, theta))
"""
Implements Linear Regression using the Gradient Descent Method.
Uses the Least Mean Squares as a cost function.
J = (1/(2*m)) * SIGMA((h - y)^2)
WORKS ONLY FOR TWO FEATURES .
DATA LOADED IS RANDOM NO RELATION --AQIDKHATKHATAY
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_4$ python3 MultiRegression.py 
[0.00563690319469732, 0.004596950486070423, 0.23706078816134735]
Accuracy: 1.0
"""



