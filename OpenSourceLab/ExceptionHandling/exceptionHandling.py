import sys
try:
	number1 = int(input("Enter a number here"))
	number2 = int(input("Enter a second number here"))
	number3 = number1/number2
except ZeroDivisionError:
	print("Pls dont enter 0 in number2, pls")
except ValueError:
	print("Pls enter Integer values, pls")
except KeyboardInterrupt:
	print("")
	print("y u close me")
else:
	print("Ay, here's your output")
	print(number3)
a = {1,2,'3'}
for x in a:
	try:
		reciprocal = 1/x
	except TypeError:
		print("Pls enter integer values in the list")
		#print(sys.exc_info()[0])
	else:
		print(reciprocal)
'''try:
	print(sys.version)
	title = input("Enter a book title: ")
	author = input("Enter the book's author: ")
	print('The book you entered is \'' + title + '\' by ' + author + '.')
except EOFError as error:
	print(error)'''
    