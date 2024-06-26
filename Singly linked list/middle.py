'''Brute force approach to find the middle of a SLL
Step 1: Create a list 
Step 2: Traverse the linked list and add data in the list
Step 3: Find middle of the list and return it'''

nodes = []

#node creation
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def traverse(self):
        if self.head is None:
            print("Linked list is empty")
            return
        n = self.head
        while n is not None:
            nodes.append(n.data)
            n = n.ref

    def find_mid(self,nodes):
        print(nodes[len(nodes)/2])

        
LL3 = LinkedList()
LL3.add_begin(1)
LL3.add_begin(2)
LL3.add_begin(3)
LL3.add_begin(4)
LL3.traverse()
print(nodes)
LL3.find_mid(nodes)