import math
import random
import numpy as np
import sys
def clarans(points, numlocal, maxneighbor, mincost,k):
    i,N=1,len(points)
    d_mat = np.asmatrix(np.empty((k,N)))
    local_best = []
    bestnode = []
    while i<=numlocal:
        node = np.random.permutation(range(N))[:k]
        fill_distances(d_mat, points, node)     
        cls = assign_to_closest(points, node, d_mat)
        cost = total_dist(d_mat, cls)
        copy_node = node.copy()
        j = 1 
        while j<=maxneighbor:
            changing_node = copy_node.copy()
            idx = pick_random_neighbor(copy_node, N)
            update_distances(d_mat, points, copy_node, idx)            
            cls = assign_to_closest(points, copy_node, d_mat)   
            new_cost = total_dist(d_mat, cls)
            if new_cost < cost:
                cost = new_cost
                local_best = copy_node.copy()
                j = 1
                continue
            else:
                j=j+1
                if j<=maxneighbor:
                    continue
                elif j>maxneighbor:
                    if mincost>cost:
                        mincost,bestnode = cost,local_best.copy()
            i = i+1
            if i>numlocal:
                fill_distances(d_mat, points, bestnode)     
                cls = assign_to_closest(points, bestnode, d_mat)
                print ("Final cost: "+str(mincost)+" ")
                print (bestnode) 
                return cls, bestnode
            else:
                break    
def pick_random_neighbor(current_node, set_size):
    node = random.randrange(0, set_size, 1)
    while node in current_node:
        node = random.randrange(0, set_size, 1)
    current_node[random.randrange(0, len(current_node))]=node
    return random.randrange(0, len(current_node))
def dist_euc (x,y):
    return math.sqrt((x[0] - x[1])**2 + (y[0] - y[1])**2)
def assign_to_closest(points, meds, d_mat):
    cluster =[]
    for i in range(len(points)):
        if i in meds:
            cluster.append(np.where(meds==i))
            continue
        d,idx = sys.maxsize,i
        for j in range(len(meds)):
            d_tmp = d_mat[j,i]
            if d_tmp < d:
                d,idx = d_tmp,j
        cluster.append(idx)
    return cluster
def fill_distances(d_mat, points, current_node):
    for i in range(len(points)):
        for k in range(len(current_node)):
            d_mat[k,i]=dist_euc(points[current_node[k]], points[i])                
def total_dist(d_mat, cls):
    tot_dist = 0
    for i in range(len(cls)):
        tot_dist += d_mat[cls[i],i]
    return tot_dist
def update_distances(d_mat, points, node, idx):
    for j in range(len(points)):
        d_mat[idx,j]=dist_euc(points[node[idx]], points[j])

dataset=[[3.522979,5.487981],
[3.768699,5.364477],
[3.423602,5.419900],
[3.803905,5.389491],
[3.936690,5.663041],
[6.968136,7.755556],
[6.750795,7.269541],
[6.593196,7.850364],
[6.978178,7.609850],
[6.554487,7.498119],]
cls,m=clarans(dataset, 10, 3, 9999,2)
print(cls)
print(m)
"""
1. Input parameters numlocal and maxneighbor. Initialize i to 1, and mincost to a large number.
2. Set current to an arbitrary node in G_{n,k}
3. Set j to 1.
4. Consider a random neighbor S of current, and based on Equation (5) calculate the cost differential 
    of the two nodes.
5. If S has a lower cost, set current to S, and go to Step (3).
6. Otherwise, increment j by 1. If j<=maxneighbor,go to Step (4).
7. Otherwise, when j > maxneighbor, compare the cost of current with mincost. If the former is less than mincost, 
    set mincost to the cost of current, and set bestnode to current.
8. Increment i by 1. If i > numlocal, output bestnode and halt. Otherwise, go to Step (2).
"""
""" NO FIXED ANSWER----AQID KHATKHATAY
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM$ python3 clarans.py
Final cost: [[14.25046554]] 
[8 6]
[1, 1, 1, 1, 1, 1, (array([1]),), 1, (array([0]),), 1]
[8 6]
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM$ python3 clarans.py
Final cost: [[14.17452451]] 
[9 6]
[1, 1, 1, 1, 1, 1, (array([1]),), 1, 1, (array([0]),)]
[9 6]
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM$ python3 clarans.py
Final cost: [[14.20623857]] 
[6 0]
[(array([1]),), 0, 0, 0, 0, 0, (array([0]),), 0, 0, 0]
[6 0]


""""


