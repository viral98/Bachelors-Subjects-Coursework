def load():
	rules,order = {},[]
	while True:
		rule = input('Enter the productions: ')
		if rule == '':
			break
		v = rule.split('->')
		lhs = v[0].strip()
		rhs = [x.strip() for x in v[1].strip().split('|')]
		rules[lhs] = rules.get(lhs, []) + rhs
		order += [lhs]
	return order, rules
def pre_process(lhs, rhs):
	alpha,beta = [],[]
	for x in rhs:
		if x[0] == lhs:
			alpha.append(x[1:])
		else:
			beta.append(x)
	return (lhs, alpha, beta)
def eliminate_direct(rules, lhs):
	l = pre_process(lhs, rules[lhs])
	if not l:
		return None
	lhs, alpha, beta = l
	lhs_new = lhs + '^'
	rules[lhs] = []
	for b in beta:
		if b=="@":
			rules[lhs] +=[lhs_new]
		else:
			rules[lhs] += [b + lhs_new]
	for a in alpha:
		rules[lhs_new] = rules.get(lhs_new, []) + [a + lhs_new]
	rules[lhs_new] = rules.get(lhs_new, []) + ['\u03B5']
def left_recursion():
	order, rules = load()
	n = len(order)
	for i in range(n):
		flag = True
		while flag:
			flag,new,rule_i = False,[],rules[order[i]]
			for j in range(len(rule_i)):
				if rule_i[j][0] in order and order.index(rule_i[j][0]) < i:
					flag,rule_j = True,rules[rule_i[j][0]]
					for r in rule_j:
						new.append(r + rule_i[j][1:])
				else:
					new.append(rule_i[j])
			rules[order[i]] = new[:]
		eliminate_direct(rules, order[i])
	for r in rules.keys():
		print(r, '->', ' | '.join(rules[r]))
left_recursion()
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/LEFT_RECURSION$ python3 lrid.py
Enter the productions: S->Ab|b
Enter the productions: A->Sa|@
Enter the productions: 
S -> AbS^ | bS^
A -> bS^aA^ | A^
S^ -> ε
A^ -> bS^aA^ | ε
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/LEFT_RECURSION$ 
"""
