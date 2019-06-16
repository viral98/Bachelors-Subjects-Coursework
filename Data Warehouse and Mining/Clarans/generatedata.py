import numpy as np
import random

def generate_chess_board(axis_length, n, size):
    data = []
    step = axis_length / n
    if n % 2 == 0:
        num_points = size / (n**2/2)
    else:
        num_points = size / ((n**2)/2 + 1)
    for i in xrange(n):
        for j in xrange(n):
            if i % 2 == j % 2:
                for k in xrange(num_points):
                    data.append([random.randint(i*step,(i+1)*step),random.randint(j*step,(j+1)*step)])

    return np.array(data).tolist()

data=generate_chess_board(10,2,100)
file = open("dataset.txt","w") 
for item in data:
	file.write("%s,\n" % item)
file.close() 



