def find_regression_coefficients(x_coordinate,y_coordinate):
		X=Y=XY=X_2=0
		for i in range(len(x_coordinate)):
			X+=x_coordinate[i]
			Y+=y_coordinate[i]
			XY+=x_coordinate[i]*y_coordinate[i]
			X_2+=x_coordinate[i]*x_coordinate[i]
		b_0=(len(x_coordinate)*XY-X*Y)/(len(x_coordinate)*X_2-X*X)
		b_0=round(b_0,4)
		b_1=(Y-b_0*X)/(len(x_coordinate))
		b_1=round(b_1,4)
		return b_0,b_1
def predict(b_0,x_coordinate,b_1):
	return round(b_0*x_coordinate+b_1,2)
x=[55,60,65,70,80]
y=[52,54,56,58,62]
pred=int(input("Enter x to be found:"))
b_0,b_1=find_regression_coefficients(x,y)
eqn='h='+str(b_1)+'+'+str(b_0)+'x'
print("Equation of line is "+eqn)
print("Predicted value of y is "+str(predict(b_0,pred,b_1)))
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM$ python3 LinearRegression.py 
Enter x to be found:90
Equation of line is h=30.0+0.4x
Predicted value of y is 66.0

"""
