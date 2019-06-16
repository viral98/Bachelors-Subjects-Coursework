def load():
	rules = {}
	while True:
		rule = input('Enter the rule: ')
		if rule == 'EOF':
			break
		v = rule.split('=')

		# Removing left and right spaces in both lhs and rhs
		lhs = v[0].strip()
		rhs = v[1].strip()

		# Preprocessing the right hand side to see all the OR options
		rhs = [x.strip() for x in rhs.split('|')]
		# Adding the processed rule to the rules
		rules[lhs] = rules.get(lhs, []) + rhs
	return rules


def foo(variable, rules):
	result = []
	for rule in rules[variable]:
		for i in range(len(rule)):
			if rule[i] in rules.keys():  # Checking whether the first character is a terminal or a non-terminal
				temp = foo(rule[i], rules)
				# Checking whether epsilon is part of this terminal's first set
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


def first(rules):
	result = {}
	for variable in rules.keys():
		result[variable] = foo(variable, rules)
	return result


def bar(variable, rules, first_set):
	result = []
	if variable == 'S':
		result.append('$')
	variables = rules.keys()
	for t in variables: #Iterate through all variables
		for rule in rules[t]: #For all the rules belonging to that variable
			if variable in rule: #If the given variable belongs to this rule
				i = rule.index(variable) #retrive the index position
				while True:
					if i >= len(rule) - 1:  # Checking to see whether the last character has been reached
						if variable != t:
							result += bar(t, rules, first_set)
						break
					else:
						if rule[i+1] not in variables:  # terminal?
							result += rule[i+1]
							break
						temp = first_set[rule[i+1]][:]  # VERY IMP: MAKE A COPY
						if '@' in temp:  # Continue to the next variable
							temp.remove('@')
							result += temp
							i += 1
						else:  # No need to examine the characters ahead
							result += temp
							break
	return list(set(result))


def follow(rules, first_set):
	follow_set = {}
	for variable in rules.keys():
		follow_set[variable] = bar(variable, rules, first_set)
	return follow_set


def pptab(rules, first_set, follow_set):
	variables = rules.keys()
	result = {}
	for var in variables:
		result[var] = {}
		for rule in rules[var]:
			i = 0
			while True:
				if i >= len(rule) or rule[i] == '@':  # Last character reached. Use follow of parent.
					for terminal in follow_set[var]:
						result[var][terminal] = rule
					break
				c = rule[i]
				if c != '@' and c not in variables:  # Terminal?
					result[var][c] = rule  # Adding the rule to the table
					break
				f = first_set[c]  # First set of the variable
				for t in f:
					if t != '@':
						result[var][t] = rule
				if '@' in f:
					i += 1
					continue
				break
	return result


def main():
	rules = load()
	first_set = first(rules)
	follow_set = follow(rules, first_set)
	tab = pptab(rules, first_set, follow_set)
	for var in tab.keys():
		print(var)
		print(tab[var])
		print('-'*20)
main()