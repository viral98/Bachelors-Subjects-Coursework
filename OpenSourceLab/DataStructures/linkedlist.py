class node:
    def __init__(self):
        self.data = None
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        newnode = node()
        newnode.data = data
        x = self.head
        if(self.head==None):
            self.head = newnode
            self.size = self.size +1
        else:

            while x.next is not None:
                x = x.next
            x.next = newnode
            self.size = self.size +1

    def delete(self,data):
        current = self.head
        while (current.data != data and current is not None):
            prev = current
            current = current.next
        if(current==None):
            print("Data not found")
        elif(current==self.head):
            self.head = current.next
            self.size = self.size -1
        elif(current==self.tail):
            self.tail = prev
            prev.next = None
            self.size = self.size -1
        else:
            prev.next = current.next
            self.size = self.size -1

    def display(self):
        x = self.head
        if(self.head==None):
            print("Empty Linked List")
        else:
            while x.next is not None:
                print (x.data)
                x = x.next
            print(x.data)

#Menu
linked = linkedList()
x=0
while(x!=4):
    x = int(input("Enter 1 to Insert at the end or 2 to delete particular data 3 to display"))
    if(x==1):
        data = int(input("Enter data to be inserted"))
        linked.insert(data)
    elif(x==2):
        data = int(input("Enter data to be Deleted"))
        linked.delete(data)
    elif(x==3):
        linked.display()