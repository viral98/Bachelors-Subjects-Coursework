colors = ('red', 'blue', 'green')
print ("First element " + colors[0])
print ("Third Element " + colors[2])
print ("Length:  ")
print (len(colors))
numbers = (1,2,23,19,5,6,7,8,9,10)
print(numbers)
sum = 0
for num in numbers:
	sum += num
print("The sum is ")
print(sum)
x = input("Enter a color to search")
if x in colors:
	print("Element Found!")
else:
	print("Element not found")
print("Slicing 1:3 in numbers...")
print(numbers[1:3])


