rules,stack,flag = {},'$',1
prod = raw_input('Enter the production rules: ').split('->')
rules[prod[0]] = prod[1].split('|')
print(rules.keys())
print(rules)

lhs = [k for k in rules.keys()]
lhs = ''.join(lhs)
ip = raw_input('Enter string to be parsed: ') + '$'

print('Stack\t\tInput\t\tAction')
while len(ip) != 1 or stack != ('$' + lhs):
	if len(stack) == 1 and len(ip) != 1:
		stack += ip[0] #Take the top most element on input
		ip = ip[1:] #Make input equal to everything within input except for first element
		print('{}\t\t{}\t\t{}'.format(stack, ip, 'Shift')) #categorize this as a shift
	temp = ''
	for i in rules.keys():
		for j in rules[i]:
			if j in stack:
				temp = j #If you find some prod rule which matches with the elements in stack
				break
	if temp:
		stack = stack.replace(temp, lhs) #Replace them
		print('{}\t\t{}\t\t{}  {}->{}'.format(stack, ip, 'Reduce', lhs, temp))
	else:	
		if ip[0]=="$": #If all the input elements have been traversed once
			flag=0		
			break
		stack += ip[0] #Shift everything that's left onto the stack
		ip = ip[1:]
		print('{}\t\t{}\t\t{}'.format(stack, ip, 'Shift'))
if flag!=0:
	print('String is accepted')
else:
	print('String is rejected')

"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC$ python SHIFTREDUCE.py 
Enter the production rules: E->E+E|E*E|i
['E']
{'E': ['E+E', 'E*E', 'i']}
Enter string to be parsed: i*i+i
Stack		Input		Action
$i		*i+i$		Shift
$E		*i+i$		Reduce  E->i
$E*		i+i$		Shift
$E*i		+i$		Shift
$E*E		+i$		Reduce  E->i
$E		+i$		Reduce  E->E*E
$E+		i$		Shift
$E+i		$		Shift
$E+E		$		Reduce  E->i
$E		$		Reduce  E->E+E
String is accepted
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC$ python SHIFTREDUCE.py 
Enter the production rules: E->E+E|E*E|(E)|i
['E']
{'E': ['E+E', 'E*E', '(E)', 'i']}
Enter string to be parsed: (i+i*i
Stack		Input		Action
$(		i+i*i$		Shift
$(i		+i*i$		Shift
$(E		+i*i$		Reduce  E->i
$(E+		i*i$		Shift
$(E+i		*i$		Shift
$(E+E		*i$		Reduce  E->i
$(E		*i$		Reduce  E->E+E
$(E*		i$		Shift
$(E*i		$		Shift
$(E*E		$		Reduce  E->i
$(E		$		Reduce  E->E*E
String is rejected
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC"""
