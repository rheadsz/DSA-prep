class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head = None

    #traversal of the linked list
    def printLL(self):
        #check if LL is empty:
        if self.head is None:
            print("Linked list is empty")
        
        n = self.head
        while n is not None:
            print(n.data,end="->" if n.ref is not None else "\n")
            n = n.ref

    #add in the beginning of the LL
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    #add before a node in the LL
    def add_before(self, before, data):
        new_node = Node(data)
        n = self.head
        while n is not None:
            if n.ref.data == before:
                new_node.ref = n.ref
                n.ref = new_node
                return
            n = n.ref

    #add after a node
    def add_after(self,after, data):
        new_node = Node(data)
        n = self.head
        while n is not None:
            if n.data == after:
                new_node.ref = n.ref
                n.ref = new_node
                return
            n = n.ref

    #add at the end
    def add_end(self,end, data):
        new_node = Node(data)
        n = self.head
        while n is not None:
            if n.ref is None:
                new_node.ref = n.ref
                n.ref = new_node
                return
            n = n.ref

    #delete first node
    def delete_first(self):
        self.head = self.head.ref

    #delete the last node
    def delete_last(self):
        n = self.head
        while n is not None:
            if n.ref.ref is None:
                n.ref = None
                return
            n = n.ref

    #delete a random node
    def delete_between(self,data):
        n = self.head
        while n is not None:
            if n.ref.data == data:
                n.ref = n.ref.ref
                return 
            n = n.ref



    


LL2 = Linkedlist()
LL2.printLL()
LL2.add_begin(1)
LL2.printLL()
LL2.add_begin(2)
LL2.printLL()
LL2.add_begin(4)
LL2.printLL()
LL2.add_before(2,3)
LL2.printLL()
LL2.add_after(3,5)
LL2.printLL()
LL2.add_end(1,6)
LL2.printLL()
print("Deleting operations")
LL2.delete_first()
LL2.printLL()
LL2.delete_last()
LL2.printLL()
LL2.delete_between(5)
LL2.printLL()
        


    

