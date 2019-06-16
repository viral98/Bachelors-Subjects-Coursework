num = 0
x = int(input("Enter Number"))
for i in range(1,x):
	
	for j in range (x,i,-1):
		print(" ", end="")

	for k in range(0,i):
		print("*", end="")
		
	print("")

for i in range(x,0,-1):

	for j in range (i,x):
		print(" ", end="")

	for k in range(i,0,-1):
		print("*", end="")
	
	print("")

		

	


