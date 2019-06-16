from math import sqrt
def compute_hits(G,n,max_iter,hubs,auth):
        prevhubs =prevauth=[0 for i in range(n)]
        for i in range(max_iter):
            prevhubs ,prevauth= hubs,auth
            auth = [0 for i in range(n)]
            for i in range(n):
                for j in range(n):
                    if G[j][i] == 1:
                        auth[i] += hubs[j]
            hubs = [0 for i in range(n)]
            for i in range(n):
                for j in range(n):
                    if G[i][j] == 1:
                        hubs[i] += auth[j]
            auth,hubs = [x / sqrt(sum([x**2 for x in auth])) for x in auth],[x /sqrt(sum([x**2 for x in hubs])) for x in hubs]
        return hubs,auth
G=[[0, 1, 1], [1, 0, 1], [1, 1, 0]]
print("Adjacency Matrix is ",G)
hubs =auth= [1 for i in range(len(G[0]))]
hubs,auth=compute_hits(G,len(G[0]),1,hubs,auth)
print(' HUB SCORE: ',hubs,'\n','AUTHORITY SCORE: ',auth)
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_9$ python3 hits.py 
Adjacency Matrix is  [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
 HUB SCORE:  [0.5773502691896258, 0.5773502691896258, 0.5773502691896258] 
 AUTHORITY SCORE:  [0.5773502691896258, 0.5773502691896258, 0.5773502691896258]
"""
