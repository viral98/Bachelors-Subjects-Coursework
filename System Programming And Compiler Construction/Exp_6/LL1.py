def get_first(variable, rules):
	result = []
	for rule in rules[variable]:
		for i in range(len(rule)):
			if rule[i] in rules.keys(): #Eg if A->B then we search for the first of B
				temp = get_first(rule[i], rules)
				if i < (len(rule) - 1) and '@' in temp: 
					temp.remove('@')
					result += temp
				else:
					result += temp
					break
			else:
				result.append(rule[i]) #Eg if A->b we just append b as the first of A
				break
	return list(set(result))
def first(rules):
	result = {}
	for variable in rules.keys():
		result[variable] = get_first(variable, rules) #Here result contains the first of every variable
	return result


def get_follow(variable, rules, first_set):
	result = []
	if variable == 'S'or variable == 'E': #if the variable is the starting variable
		result.append('$')
	variables = rules.keys()
	for t in variables: #For a variable in all the variables
		for rule in rules[t]: #For a rule in that variable
			if variable in rule: #If the original variable we are looking out for is here
				i = rule.index(variable) #Get its index
				while True:
					if i >= len(rule) - 1:  
						if variable != t:
							result += get_follow(t, rules, first_set)
						break
					else:
						if rule[i+1] not in variables: 
							result += rule[i+1]
							break
						temp = first_set[rule[i+1]][:]
						if '@' in temp:  
							temp.remove('@')
							result += temp
							i += 1
						else: 
							result += temp
							break	
	return list(set(result))

def follow(rules, first_set):
	follow_set = {}
	for variable in rules.keys():
		follow_set[variable] = get_follow(variable, rules, first_set)
	return follow_set


def pptab(rules, first_set, follow_set):
	variables = rules.keys()
	result = {}
	for var in variables:
		result[var] = {}
		for rule in rules[var]:
			i = 0
			while True:
				if i >= len(rule) or rule[i] == '@': 
					for terminal in follow_set[var]:
						result[var][terminal] = var+"->"+rule
					break
				c = rule[i]
				if c != '@' and c not in variables: 
					result[var][c] = var+"->"+rule 
					break
				f = first_set[c]  
				for t in f:
					if t != '@':
						result[var][t] = var+"->"+rule
				if '@' in f:
					i += 1
					continue
				break
	return result

#rules ={'S': ['AC'], 'C': ['c', '@'], 'A': ['aBCd', 'BQ', '@'], 'B': ['bB', 'd'], 'Q': ['d']}
rules={'E':['TX'],'X':['+TX','@'],'T':['FY'],'Y':['*FY','@'],'F':['(E)','id']}
print("rules ",rules)
first_set = first(rules)
follow_set = follow(rules, first_set)
print("First Set ",first_set)
print("Follow Set ",follow_set)
tab = pptab(rules, first_set, follow_set)
for var in tab.keys():
	print(var)
	print(tab[var])
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_6$ python3 LL1.py
rules  {'E': ['TX'], 'X': ['+TX', '@'], 'T': ['FY'], 'Y': ['*FY', '@'], 'F': ['(E)', 'id']}
First Set  {'E': ['i', '('], 'X': ['@', '+'], 'T': ['i', '('], 'Y': ['@', '*'], 'F': ['i', '(']}
Follow Set  {'E': ['$', ')'], 'X': ['$', ')'], 'T': ['$', '+', ')'], 'Y': ['$', '+', ')'], 'F': ['*', '$', '+', ')']}
E
{'i': 'E->TX', '(': 'E->TX'}
X
{'+': 'X->+TX', '$': 'X->@', ')': 'X->@'}
T
{'i': 'T->FY', '(': 'T->FY'}
Y
{'*': 'Y->*FY', '$': 'Y->@', '+': 'Y->@', ')': 'Y->@'}
F
{'(': 'F->(E)', 'i': 'F->id'}
"""


