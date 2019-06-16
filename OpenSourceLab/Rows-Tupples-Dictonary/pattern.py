num = 0
x = int(input("Enter Number"))

for i in range(1,x):

	for j in range (x,i,-1):
		print(" ", end="")

	num = int((i*(i+1))/2)

	for k in range(0,i):
		print(int(num), end="")
		num = num -1


	print("")	
		

	


