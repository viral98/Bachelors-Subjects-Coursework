class Node:
    def __init__(self):
        self.num_children = 0
        self.children = []
        self.parent = None
        self.times = 0
        self.item = ''


def BuildTree(node, list, element):
    if(len(list) == 0):
        return
    for child in node.children:
        if(child.item == element):
            child.times += 1
            del list[0]
            if(len(list) == 0):
                return
            BuildTree(child, list, list[0])
            if(len(list) == 0):
                return
            break
    new_node = Node()
    node.num_children += 1
    new_node.times += 1
    new_node.item, new_node.parent = element, node
    node.children.append(new_node)
    del list[0]
    if(len(list) == 0):
        return
    BuildTree(new_node, list, list[0])


def Draw_tree(node, prefix, isTail):
    if(isTail):
        temp = prefix+"L_"+node.item
    else:
        temp = prefix+"|-- "+node.item
    print(temp+"("+str(node.times)+")")
    for n in range(0, len(node.children)-1):
        if(isTail):
            Draw_tree(node.children[n], prefix+"    ", False)
        else:
            Draw_tree(node.children[n], prefix+"|   ", False)
    if(len(node.children) >= 1):
        if(isTail):
            prefix = prefix+"    "
        else:
            prefix = prefix+"|   "
        Draw_tree(node.children[-1], prefix, True)


def FindA(node, a, list):
    if(len(node.children) == 0):
        return
    if(node.item == a):
        list.append(node)
    else:
        for child in node.children:
            FindA(child, a, list)


def FindB(node, b, list):
    if(node.item == b):
        list.append(node)
    else:
        for child in node.children:
            FindB(child, b, list)
        if(len(node.children) == 0):
            return


def ordered_frequent_items(filename, listname, minsup):
    file = open('transaction1.txt')
    num_of_line = len(file.readlines())
    Ordered_list = [[] for i in range(num_of_line)]
    n = 0
    for line in filename:
        for character in listname:
            for element in line:
                if(character == element):
                    Ordered_list[n].append(character)
                    print(Ordered_list[n])
        print (Ordered_list[n])
        n = n+1
    return Ordered_list


file = open('transaction1.txt')
minimum_support = input("Please input a minimum support: ")
sample_list = ['f', 'c', 'a', 'b', 'm', 'p']
Ordered_list = ordered_frequent_items(file, sample_list, minimum_support)
root = Node()
for n in Ordered_list:
    BuildTree(root, n, n[0])
Draw_tree(root, "", True)
print(ordered_frequent_items(file, sample_list, minimum_support))
temp = input("Please input 2 items: ")
a, b = temp[0], temp[1]
for element in sample_list:
    if(element == a):
        break
    elif(element == b):
        temp, a, b = a, b, temp
        break
    else:
        break
result, A_list, B_list = 0, [], []
FindA(root, a, A_list)
for node in A_list:
    FindB(node, b, B_list)
for node in B_list:
    result += node.times
print(result)
"""

TECHMAX PAGE 5-35 EXAMPLE 
INPUT IS HARDCODED TO SAVE TIME 
DOES NOT WORK FOR UPPER CASE INPUT OR NUMBERS .INPUT ONLY LOWER CASE
REMOVE THE LAST LINES IF ONLY TREE IS REQUIRED AND NO CONDITIONAL FP 
ALSO REMOVE FindA and FindB 
ORDERED FREQUENT CODE CAN ALSO BE PUT AS FOLLOWS


--AQID KHATKHATAY

def ordered_frequent_items(filename, listname):#find the frequent items of users
	file=open('transactions.txt')
	num_of_line=len(file.readlines())
	Ordered_list = [[] for i in range(num_of_line)]
	n=0
	for line in filename:
		for character in listname:
			for element in line:
				if(character==element):
					Ordered_list[n].append(character)
		print Ordered_list[n]
		n=n+1
	return Ordered_list

IN MAIN
Ordered_list=ordered_frequent_items(file, sample_list)
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/FP_TREE$ python3 fp_growth.py 
Please input a minimum support: 2
['f']
['f', 'c']
['f', 'c', 'a']
['f', 'c', 'a', 'm']
['f', 'c', 'a', 'm', 'p']
['f', 'c', 'a', 'm', 'p']
['f']
['f', 'c']
['f', 'c', 'a']
['f', 'c', 'a', 'b']
['f', 'c', 'a', 'b', 'm']
['f', 'c', 'a', 'b', 'm']
['f']
['f', 'b']
['f', 'b']
['c']
['c', 'b']
['c', 'b', 'p']
['c', 'b', 'p']
['f']
['f', 'c']
['f', 'c', 'a']
['f', 'c', 'a', 'm']
['f', 'c', 'a', 'm', 'p']
['f', 'c', 'a', 'm', 'p']
L_(0)
    |-- f(4)
    |   |-- c(3)
    |   |   L_a(3)
    |   |       |-- m(2)
    |   |       |   L_p(2)
    |   |       L_b(1)
    |   |           L_m(1)
    |   L_b(1)
    L_c(1)
        L_b(1)
            L_p(1)
[[], [], [], [], []]
Please input 2 items: cp
3
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/FP_TREE$ 

"""
