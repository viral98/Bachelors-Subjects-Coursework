def first(rules):
	result = {}
	for variable in rules.keys():
		result[variable] = get_first(variable, rules)
	return result
def get_first(variable, rules):
	result = []
	for rule in rules[variable]:
		for i in range(len(rule)):
			if rule[i] in rules.keys(): 
				temp = get_first(rule[i], rules)
				if i < (len(rule) - 1) and '@' in temp:
					temp.remove('@')
					result += temp
				else:
					result += temp
					break
			else:
				result.append(rule[i])
				break
	return list(set(result))
def follow(rules, first_set):
	follow_set = {}
	for variable in rules.keys():
		follow_set[variable] = get_follow(variable, rules, first_set)
	return follow_set
def get_follow(variable, rules, first_set):
	result = []
	if variable == 'S'or variable == 'E':
		result.append('$')
	variables = rules.keys()
	for t in variables:
		for rule in rules[t]:
			if variable in rule:
				i = rule.index(variable)
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
#rules ={'S': ['AC'], 'C': ['c', '@'], 'A': ['aBCd', 'BQ', '@'], 'B': ['bB', 'd'], 'Q': ['d']}
rules={'E':['TX'],'X':['+TX','@'],'T':['FY'],'Y':['*FY','@'],'F':['(E)','id']}
print("rules ",rules)
print("First Set ",first(rules))
print("Follow Set ",follow(rules, first(rules)))
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_5$ python3 FirstFollow.py 
rules  {'S': ['AC'], 'C': ['c', '@'], 'A': ['aBCd', 'BQ', '@'], 'B': ['bB', 'd'], 'Q': ['d']}
First Set  {'S': ['@', 'd', 'c', 'a', 'b'], 'C': ['@', 'c'], 'A': ['@', 'd', 'a', 'b'], 'B': ['d', 'b'], 'Q': ['d']}
Follow Set  {'S': ['$'], 'C': ['d', '$'], 'A': ['$', 'c'], 'B': ['d', 'c'], 'Q': ['$', 'c']}
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_5$ python3 FirstFollow.py 
rules  {'E': ['TX'], 'X': ['+TX', '@'], 'T': ['FY'], 'Y': ['*FY', '@'], 'F': ['(E)', 'id']}
First Set  {'E': ['i', '('], 'X': ['@', '+'], 'T': ['i', '('], 'Y': ['*', '@'], 'F': ['i', '(']}
Follow Set  {'E': [')', '$'], 'X': [')', '$'], 'T': [')', '+', '$'], 'Y': [')', '+', '$'], 'F': [')', '*', '+', '$']}
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_5$ 
"""
