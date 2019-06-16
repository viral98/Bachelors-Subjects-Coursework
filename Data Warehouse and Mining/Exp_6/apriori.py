from itertools import combinations
def base_set(transactions):
	ans = set()
	for t in transactions:
		for item in t:
			ans.add(item)
	return ans
def support(transactions, combination):
	count = 0
	for t in transactions:
		if set(combination).issubset(set(t)):
			count += 1
	return count
def iteration(all_items, transactions, disallowed, size, min_support, min_confidence):
	temp ,a= [],0
	for c in combinations(all_items, size):
		flag = True
		for d in disallowed:
			if d in list(c):
				flag = False
		if flag:
			temp.append(list(c))
	for combination in temp:
		if support(transactions, combination) >= min_support:
			print("Generating Association rules for frequent itemset", combination)
			gen_rules(transactions, combination, min_confidence)
def apriori(transactions, min_support, min_confidence):
	all_items = base_set(transactions)
	disallowed = []
	for i in range(1, len(all_items)+1):
		iteration(all_items, transactions, disallowed, i, min_support, min_confidence)
	return None
def gen_rules(transactions, freq_itemset, min_confidence):
	freq_itemset = set(freq_itemset)
	for i in range(1, len(freq_itemset)):
		for subset in combinations(freq_itemset, i):
			lhs = set(subset)
			rhs = freq_itemset - set(lhs)
			if len(lhs) >= 1 and len(rhs) >= 1 and confidence(transactions, lhs, rhs) >= min_confidence:
				print("Association Rule:", lhs, '->', rhs)
	return None
def confidence(transactions, lhs, rhs):
	num,den = 0,0
	for t in transactions:
		if lhs.issubset(set(t)):
			den += 1
			if rhs.issubset(set(t)):
				num += 1
	return (num/den)
min_support = 2
min_confidence =0.80
transactions=[['bread','jelly','butter'],['bread','butter'],['bread','milk','butter'],['coke','bread'],['coke','milk']]
#transactions=[['A', 'C', 'D'], ['B', 'C', 'E'], ['A', 'B', 'C', 'E'], ['B', 'E']]
"""transactions=[['A','B','C', 'D'],
 ['A','B','C', 'D','E','G'],
['A','C', 'G','H','K'], 
['B','C','D','E','K'], ['D','E','F','H','L'],['A','B','C', 'D','L'],['B','I','E','K','L'],
['A','B','D','E','K'],['A','E','F', 'H','L'],['B','C','D','F']]"""
apriori(transactions, min_support, min_confidence)
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM$ python3 pap.py
Generating Association rules for frequent itemset ['E']
Generating Association rules for frequent itemset ['C']
Generating Association rules for frequent itemset ['B']
Generating Association rules for frequent itemset ['A']
Generating Association rules for frequent itemset ['E', 'C']
Generating Association rules for frequent itemset ['E', 'B']
Association Rule: {'E'} -> {'B'}
Association Rule: {'B'} -> {'E'}
Generating Association rules for frequent itemset ['C', 'B']
Generating Association rules for frequent itemset ['C', 'A']
Association Rule: {'A'} -> {'C'}
Generating Association rules for frequent itemset ['E', 'C', 'B']
Association Rule: {'E', 'C'} -> {'B'}
Association Rule: {'C', 'B'} -> {'E'}
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM$ python3 pap.py
Generating Association rules for frequent itemset ['D']
Generating Association rules for frequent itemset ['H']
Generating Association rules for frequent itemset ['E']
Generating Association rules for frequent itemset ['K']
Generating Association rules for frequent itemset ['F']
Generating Association rules for frequent itemset ['C']
Generating Association rules for frequent itemset ['A']
Generating Association rules for frequent itemset ['B']
Generating Association rules for frequent itemset ['L']
Generating Association rules for frequent itemset ['D', 'E']
Generating Association rules for frequent itemset ['D', 'C']
Association Rule: {'D'} -> {'C'}
Association Rule: {'C'} -> {'D'}
Generating Association rules for frequent itemset ['D', 'A']
Generating Association rules for frequent itemset ['D', 'B']
Association Rule: {'D'} -> {'B'}
Association Rule: {'B'} -> {'D'}
Generating Association rules for frequent itemset ['E', 'K']
Association Rule: {'K'} -> {'E'}
Generating Association rules for frequent itemset ['E', 'A']
Generating Association rules for frequent itemset ['E', 'B']
Generating Association rules for frequent itemset ['E', 'L']
Association Rule: {'L'} -> {'E'}
Generating Association rules for frequent itemset ['K', 'B']
Association Rule: {'K'} -> {'B'}
Generating Association rules for frequent itemset ['C', 'A']
Generating Association rules for frequent itemset ['C', 'B']
Association Rule: {'C'} -> {'B'}
Association Rule: {'B'} -> {'C'}
Generating Association rules for frequent itemset ['A', 'B']
Generating Association rules for frequent itemset ['D', 'E', 'B']
Association Rule: {'D', 'E'} -> {'B'}
Association Rule: {'E', 'B'} -> {'D'}
Generating Association rules for frequent itemset ['D', 'C', 'A']
Association Rule: {'D', 'A'} -> {'C'}
Association Rule: {'C', 'A'} -> {'D'}
Generating Association rules for frequent itemset ['D', 'C', 'B']
Association Rule: {'D'} -> {'C', 'B'}
Association Rule: {'B'} -> {'D', 'C'}
Association Rule: {'C'} -> {'D', 'B'}
Association Rule: {'D', 'B'} -> {'C'}
Association Rule: {'D', 'C'} -> {'B'}
Association Rule: {'C', 'B'} -> {'D'}
Generating Association rules for frequent itemset ['D', 'A', 'B']
Association Rule: {'D', 'A'} -> {'B'}
Association Rule: {'B', 'A'} -> {'D'}
Generating Association rules for frequent itemset ['E', 'K', 'B']
Association Rule: {'K'} -> {'E', 'B'}
Association Rule: {'E', 'B'} -> {'K'}
Association Rule: {'B', 'K'} -> {'E'}
Association Rule: {'E', 'K'} -> {'B'}
Generating Association rules for frequent itemset ['C', 'A', 'B']
Association Rule: {'C', 'A'} -> {'B'}
Association Rule: {'B', 'A'} -> {'C'}
Generating Association rules for frequent itemset ['D', 'C', 'A', 'B']
Association Rule: {'D', 'A'} -> {'C', 'B'}
Association Rule: {'B', 'A'} -> {'D', 'C'}
Association Rule: {'C', 'A'} -> {'D', 'B'}
Association Rule: {'D', 'B', 'A'} -> {'C'}
Association Rule: {'D', 'A', 'C'} -> {'B'}
Association Rule: {'C', 'B', 'A'} -> {'D'}
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM$ 
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_6$ python3 apriori.py 
Generating Association rules for frequent itemset ['bread']
Generating Association rules for frequent itemset ['coke']
Generating Association rules for frequent itemset ['milk']
Generating Association rules for frequent itemset ['butter']
Generating Association rules for frequent itemset ['bread', 'butter']
Association Rule: {'butter'} -> {'bread'}
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_6$ 



"""
