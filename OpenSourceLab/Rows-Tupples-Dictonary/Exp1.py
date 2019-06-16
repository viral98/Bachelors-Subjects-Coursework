x = 1
while x==1:
	var1 = input("Enter a string")
	var2 = input("Enter another string")
	var3 = var1+var2
	choice = int(input("Enter 1 to find something\n2. to split the string\n3. to Replace characters\n 4. to perform Join Operation\n"))
	if (choice==1):
		inputChar = input("Enter the character")
		intChoice = int(input("Enter 1 to reverse search for an occurance of a character\n2 to check if the string starts with the given alphabet\n3 to use index function"))
		if (intChoice==1):
			print ("The output is ")
			print (var3.rfind(inputChar))
		elif (intChoice==2):
			print (var3.startswith( inputChar ))
		else:
			print ("The output is ")
			print (var3.rindex(inputChar))
	elif (choice==2):
		print (var3.split(" "))
	elif (choice==3):
		inputChar = input("Enter the character to replace")
		inputChar2 = input("Enter the character")
		print (var3.replace(inputChar, inputChar2))
	elif(choice == 4):
		inputChar = input("Enter a seperator")
		print(var3.join(inputChar))
	x = int(input("Enter 1 to Continue"))


