class node:
    def __init__(self):
        self.data = None
        self.next = None


class linkedList:
    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0

    def enqueue(self, data):
        newnode = node()
        newnode.data = data
        x = self.rear
        if(x is None):
            self.rear = newnode
            self.front = newnode
            newnode.next = None
        else:
            x.next = newnode
            self.rear = newnode
        self.size = self.size +1


    def dequeue(self):
        current = self.front
        if(current is not None):
            self.front = current.next
            self.size = self.size -1
        else:
            print("Queue out of elements")

    def display(self):
        x = self.front
        if(x==None):
            print("Nothing to display")
        else:
            while x.next is not None:
                print (x.data)
                x = x.next
            print(x.data)

#Menu
linked = linkedList()
x=0
while(x!=4):
    x = int(input("Enter 1 to enqueue or 2 to dequeue 3 to display"))
    if(x==1):
        data = int(input("Enter data to be enqueue"))
        linked.enqueue(data)
    elif(x==2):
        linked.dequeue()
    elif(x==3):
        linked.display()