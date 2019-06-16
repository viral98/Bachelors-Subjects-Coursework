

import math
import random
import numpy as np
import sys
import ast
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

def clarans_basic(points, numlocal, maxneighbor, mincost,k):
#    random.seed(1)
#    np.random.seed(1)
    i=1
    N = len(points)
    d_mat = np.asmatrix(np.empty((k,N)))
    local_best = []
    bestnode = []
    
    while i<=numlocal:
        #Step 2 - pick k random medoids from data points - medoids_nr from points
        node = np.random.permutation(range(N))[:k]
        fill_distances(d_mat, points, node)     
        cls = assign_to_closest(points, node, d_mat)   
        cost = total_dist(d_mat, cls)
        copy_node = node.copy()
        print ' \n New start '
        #increase neighbor count
        j = 1 
        
        while j<=maxneighbor:
            #Step 4 - pick a random neighbor of current node - i.e change randomly one medoid
            #calculate the cost differential of the initial node and the random neighbor
            changing_node = copy_node.copy()
            idx = pick_random_neighbor(copy_node, N)
            update_distances(d_mat, points, copy_node, idx)            
            cls = assign_to_closest(points, copy_node, d_mat)   
            new_cost = total_dist(d_mat, cls)
            
            #check if new cost is smaller 
            if new_cost < cost:
                cost = new_cost
                local_best = copy_node.copy()
                print 'Best cost: ' + str(cost) + ' '
                print local_best 
                j = 1
                continue
            else:
                #copy_node = changing_node
                j=j+1
                if j<=maxneighbor:
                    continue
                elif j>maxneighbor:
                    if mincost>cost:
                        mincost = cost
                        print "change bestnode " 
                        print bestnode
                        print " into"
                        bestnode = local_best.copy()
                        print bestnode
                        
            i = i+1
            if i>numlocal:
                fill_distances(d_mat, points, bestnode)     
                cls = assign_to_closest(points, bestnode, d_mat)
                print "Final cost: " + str(mincost) + ' '
                print bestnode 
                return cls, bestnode
            else:
                break
    
    
def pick_random_neighbor(current_node, set_size):
    #pick a random item from the set and check that it is not selected
    node = random.randrange(0, set_size, 1)
    while node in current_node:
        node = random.randrange(0, set_size, 1)
        
    #replace a random node
    i = random.randrange(0, len(current_node))
    current_node[i]=node
    return i
    
def dist_euc((x1, y1), (x2, y2)):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def assign_to_closest(points, meds, d_mat):
    cluster =[]
    for i in xrange(len(points)):
        if i in meds:
            cluster.append(np.where(meds==i))
            continue
        d = sys.maxint
        idx=i
        for j in xrange(len(meds)):
            d_tmp = d_mat[j,i]
            if d_tmp < d:
                d = d_tmp
                idx=j
        cluster.append(idx)
    return cluster


def fill_distances(d_mat, points, current_node):
    for i in range(len(points)):
        for k in range(len(current_node)):
            d_mat[k,i]=dist_euc(points[current_node[k]], points[i])
        
        
def total_dist(d_mat, cls):
    tot_dist = 0
    for i in xrange(len(cls)):
        tot_dist += d_mat[cls[i],i]
    return tot_dist


def update_distances(d_mat, points, node, idx):
    for j in range(len(points)):
        d_mat[idx,j]=dist_euc(points[node[idx]], points[j])

dataset=[]
file=open("dataset.txt","r")
for line in file:
	lin=line[:-2]
	linlist=ast.literal_eval(lin)
	dataset.append(linlist)

cls,m=clarans_basic(dataset, 5, 10, 250,8)


