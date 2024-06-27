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

    def add_after(self,data,after_node):
        new_node = Node(data)
        n = self.head
        while n is not None:
            if n.data == after_node:
                if n.next is None:
                    n.next = new_node
                    new_node.prev = n
                    return
                
                new_node.prev = n
                n.next.prev = new_node
                new_node.next = n.next
                n.next = new_node
                return
            n = n.next

    def add_before(self,data,before_node):
        new_node = Node(data)
        n = self.head
        while n is not None:
            if n.data == before_node:
                if n.prev is None:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                    return
                new_node.next = n.prev.next
                new_node.prev = n.prev
                n.prev.next = new_node     
                return
            n = n.next

    def delete_begin(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            return
        n = self.head
        while n is not None:
            if n.next is None and n.prev is not None:
                n.prev.next = n.next
                return
            elif n.next is None and n.prev is None:
                self.head = None
                return
            else:
                n = n.next

    def delete_between(self,data):
        n = self.head
        while n is not None:
            if n.data == data:
                n.prev.next = n.next
                n.next.prev = n.prev
                return 
            n = n.next

dl = DoublyLinkedlist()
dl.add_begin(1)
dl.delete_end()
dl.traverse_forward()
dl.add_begin(2)
dl.add_begin(3)
dl.add_end(4)
dl.add_after(5,3)
dl.add_before(6,2)
dl.add_after(7,4)
dl.add_before(8,3)
dl.delete_begin()
dl.traverse_forward()
dl.delete_end()
dl.delete_between(6)
dl.traverse_forward()
dl.traverse_backward()
