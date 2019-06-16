count = 0
def left_factoring(s):
    v = s.split('->')
    lhs= v[0].strip()
    rhs = [x.strip() for x in v[1].strip().split('|')]
    factor(lhs, rhs)
def factor(lhs, rhs):
    l=[]
    visited,variables,beta = [0 for i in rhs],{},[]
    for i in range(len(rhs)):
        if visited[i] == 0:
            flag,visited[i],rule = 0,1,rhs[i]
            for j in range(i+1, len(rhs)):
                if visited[j] == 0 and (rule[0] == rhs[j][0]):
                    visited[j] = flag=1
                    variables[rule[0]] = variables.get(rule[0], []) + [rhs[j][1:]]
            if flag == 0:
                beta.append(rule)
            else:
                variables[rule[0]] = variables.get(rule[0], []) + [rule[1:]]
    global count
    for key in variables.keys():
        count += 1
        lhs_new = lhs + '^'*(count - lhs.count('^'))
        print(lhs, '->', key + lhs_new)
        factor(lhs_new, variables[key])
    for rem in beta:
        print(lhs, '->', rem)
left_factoring('A -> aB | aY |aZ| id')
left_factoring('B->aB|aC|cD|cZ|e')
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/LEFT_FACTORING$ python3 lf.py 
A -> aA^
A^ -> Y
A^ -> Z
A^ -> B
A -> id
B -> aB^^
B^^ -> C
B^^ -> B
B -> cB^^^
B^^^ -> Z
B^^^ -> D
B -> e
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/LEFT_FACTORING$ 
"""
