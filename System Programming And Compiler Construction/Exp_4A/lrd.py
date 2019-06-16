def pre_process(s):
	v = s.split('->')
	lhs = v[0].strip()
	rhs = [x.strip() for x in v[1].strip().split('|')]
	alpha,beta = [],[]
	for x in rhs:
		if x[0] == lhs:
			alpha.append(x[1:])
		else:
			beta.append(x)
	return (lhs, alpha, beta)
def eliminate(s):
	l = pre_process(s)
	if not l:
		return None
	lhs, alpha, beta = l
	lhs_new = lhs + '^'
	for b in beta:
		if b=='@':
			print(lhs,' ->',lhs_new)
		else:
			print(lhs, ' ->', b + lhs_new)
	for a in alpha:
		print(lhs_new, '->', a + lhs_new)
	print(lhs_new, '->', '\u03B5')
eliminate('E->E+E|E*E|id')
eliminate('A->Ac|Ab|@')
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/LEFT_RECURSION$ python3 lrd.py
E  -> idE^
E^ -> +EE^
E^ -> *EE^
E^ -> ε
A  -> A^
A^ -> cA^
A^ -> bA^
A^ -> ε
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/LEFT_RECURSION$ 
"""
