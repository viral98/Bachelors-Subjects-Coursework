class node:
    def __init__(self):
        self.data = None
        self.next = None


class linkedList:
    def __init__(self):
        self.top = None
        self.tail = None
        self.size = 0

    def push(self, data):
        newnode = node()
        newnode.data = data
        x = self.top
        if(x is None):
            self.top = newnode
            newnode.next = None
        else:
            newnode.next = x
            self.top = newnode
        self.size = self.size +1


    def pop(self):
        current = self.top
        if(current is not None):
            self.top = current.next
            self.size = self.size -1
        else:
            print("Underflow")

    def display(self):
        x = self.top
        if(self.top==None):
            print("Empty stack")
        else:
            while x.next is not None:
                print (x.data)
                x = x.next
            print(x.data)

#Menu
linked = linkedList()
x=0
while(x!=4):
    x = int(input("Enter 1 to push or 2 to pop 3 to display"))
    if(x==1):
        data = int(input("Enter data to be pushed"))
        linked.push(data)
    elif(x==2):
        linked.pop()
    elif(x==3):
        linked.display()