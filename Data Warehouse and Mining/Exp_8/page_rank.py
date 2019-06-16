import math
def compute_pagerank(n, L, G, max_iter, pagerank, alpha):
        prevpagerank = {i:0 for i in range(n)}
        for i in range(n):
                for j in range(n):
                    L[i] += G[i][j]
        for k in range(max_iter):
            prevpagerank = pagerank
            for i in range(n):
                pagerank[i] = 0
                for j in range(n):
                    if G[j][i] == 1:
                        pagerank[i] = pagerank[i] + 1.0 * prevpagerank[j] / L[j] if L[j] else 1.0/n
                pagerank[i] = ((1 - alpha) * 1.0)/n + alpha * (pagerank[i])
        return pagerank
G=[[0, 1, 1], [1, 0, 1], [1, 1, 0]]
print("Adjacency Matrix is ",G)
pagerank={i:1.0/len(G[0]) for i in range(len(G[0]))}
L = [0 for i in range(len(G[0]))]
pagerank = compute_pagerank(len(G[0]),L,G,1,pagerank,0.85)
sorted_pr = sorted([(value, key) for (key,value) in pagerank.items()],reverse=True)
print(sorted_pr)
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_8$ python3 page_rank.py 
Adjacency Matrix is  [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
[(0.3333333333333333, 2), (0.3333333333333333, 1), (0.3333333333333333, 0)]
"""
