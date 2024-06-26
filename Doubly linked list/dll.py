class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedlist:
    def __init__(self):
        self.head = None

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n


    def traverse_forward(self):
        if self.head is None:
            print("Doubly Linked list is empty")
        n = self.head
        while n is not None:
            print(n.data,end="->" if n.next is not None else "\n")
            n = n.next
    
    def traverse_backward(self):
        if self.head is None:
            print("Doubly Linked list is empty")
        n = self.head
        while n.next is not None:
            n = n.next
        #here n reaches the last node in the DLL
        while n is not None:
            print(n.data,end="->" if n.prev is not None else "\n")
            n = n.prev

dl = DoublyLinkedlist()
dl.add_begin(1)
dl.add_begin(2)
dl.add_begin(3)
dl.add_end(4)
dl.traverse_forward()
dl.traverse_backward()