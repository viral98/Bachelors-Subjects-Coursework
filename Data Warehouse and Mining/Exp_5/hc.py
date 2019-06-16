def check(graph,symb):
    min=999
    for i in symb:
        for j in graph[i]:
            if(graph[i][j]<min):
                min,t1,t2=graph[i][j],i,j
    return t1,t2,min
def singlelink(graph,symb,t1,t2):
    graph[t1+t2]={}
    for i in symb:
        if i!=t1 and i!=t2:
            graph[t1+t2][i]=999
            for j in graph[i]:
                if(j==t1 or j==t2):
                    if(graph[i][j]<=graph[t1+t2][i]):
                        graph[t1+t2][i]=graph[i][j]
            graph[i][t1+t2]=graph[t1+t2][i]
            del graph[i][t1]
            del graph[i][t2]
    del graph[t1]
    del graph[t2]
    symb.append(t1+t2)
    symb.remove(t1)
    symb.remove(t2)
def averagelink(graph,symb,t1,t2):
    graph[t1+t2]={}
    for i in symb:
        if i!=t1 and i!=t2:
            graph[t1+t2][i]=(graph[i][t1]+graph[i][t2])/2
            graph[i][t1+t2]=graph[t1+t2][i]
            del graph[i][t1]
            del graph[i][t2]
    del graph[t1]
    del graph[t2]
    symb.append(t1+t2)
    symb.remove(t1)
    symb.remove(t2)
def completelink(graph,symb,t1,t2):
    graph[t1+t2]={}
    for i in symb:
        if i!=t1 and i!=t2:
            graph[t1+t2][i]=-1
            for j in graph[i]:
                if(j==t1 or j==t2):
                    if(graph[i][j]>=graph[t1+t2][i]):
                        graph[t1+t2][i]=graph[i][j]
            graph[i][t1+t2]=graph[t1+t2][i]
            del graph[i][t1]
            del graph[i][t2]
    del graph[t1]
    del graph[t2]
    symb.append(t1+t2)
    symb.remove(t1)
    symb.remove(t2)
graph={}#example techmax page 4-126 
graph['A']={'B':2,'C':6,'D':10,'E':9}
graph['B']={'A':2,'C':3,'D':9,'E':8}
graph['C']={'A':6,'B':3,'D':7,'E':5}
graph['D']={'A':10,'B':9,'C':7,'E':4}
graph['E']={'A':9,'B':8,'C':5,'D':4}
symb=['A','B','C','D','E']
while(len(symb)!=1):
    t1,t2,tl=check(graph,symb)
    print(t1+"-"+t2+"=>"+str(tl))
    averagelink(graph,symb,t1,t2)
"""
single
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_5$ python3 hc.py
A-B=>2
C-AB=>3
D-E=>4
CAB-DE=>5
complete
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_5$ python3 hc.py
A-B=>2
D-E=>4
C-AB=>6
DE-CAB=>10
average
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_5$ python3 hc.py
A-B=>2
D-E=>4
C-AB=>4.5
DE-CAB=>7.5
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_5$ 
"""
