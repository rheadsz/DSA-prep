class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):  
        if self.head is None:
            print("Linked list is empty")
        
        n = self.head
        while n is not None:
            print(n.data, end="->" if n.ref is not None else "\n")
            n = n.ref
LL1 = LinkedList()
LL1.printLL()