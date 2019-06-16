colors = ['red', 'blue', 'green']
print ("First element " + colors[0])
print ("Third Element " + colors[2])
print ("Length:  ")
print (len(colors))
colors.append("Yellow")
print("After append operation")
print ("Fourth Element " + colors[3])
print ("Length:  ")
print (len(colors))
colors.insert(2,"Pink")
print("After insert operation")
print ("Third Element " + colors[2])
print ("Length:  ")
print (len(colors))
colors.remove("Pink")
print("After remove operation")
print ("Third Element " + colors[2])
print ("Length:  ")
print (len(colors))
numbers = [1,2,23,19,5,6,7,8,9,10]
sum = 0
for num in numbers:
	sum += num
print("The sum is ")
print(sum)
print("After sorting...")
numbers.sort()
print(numbers)

