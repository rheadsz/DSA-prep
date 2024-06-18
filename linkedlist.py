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

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        #check if LL is empty
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self,old_node_data, new_node_data):
        new_node = Node(new_node_data)
        n = self.head
        while n is not None:
            if n.data == old_node_data:
                new_node.ref = n.ref
                n.ref = new_node
                break
            else:
                n = n.ref
        if n is None:
            print("Node not present in LL")
            
            
            
    def add_before(self, given_node_data, new_node_data):
        new_node = Node(new_node_data)
        if self.head is None:
            print("Linked list is empty")
            return
        #check if we are adding before the first item in the LL
        if self.head.data == given_node_data:
            new_node.ref = self.head
            self.head = new_node
            return
        else: #if we are adding between other nodes
            n = self.head
            while n is not None:
                if n.ref.data == given_node_data:
                    new_node.ref = n.ref 
                    n.ref = new_node
                    break
                else:
                    n = n.ref

    def delete_begin(self):
        #check if LL is empty
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            self.head = self.head.ref



LL1 = LinkedList()

LL1.add_begin(10)

LL1.add_begin(20)
LL1.add_end(5)
LL1.add_end(6)
LL1.printLL()
LL1.add_after(20,25)
LL1.add_after(2,28)
LL1.add_after(6,28)
LL1.add_before(6,7)
LL1.add_before(20,8)
LL1.printLL()
LL1.delete_begin()
LL1.printLL()
