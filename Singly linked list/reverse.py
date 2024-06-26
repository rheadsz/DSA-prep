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
        n = self.head
        while n is not None:
            print(n.data,end="->" if n.ref is not None else "\n" )
            n = n.ref

    #iterative approach      
    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            nxt = cur.ref
            cur.ref = prev
            prev = cur
            cur = nxt
        self.head = prev #points to the new head 

    #recursive approach
     # Recursive approach
    def recursive_reverse(self, node):
        # Base case: if node is None or node.ref is None, return node
        if node is None or node.ref is None:
            return node

        # Recursive case: reverse the rest of the list
        new_head = self.recursive_reverse(node.ref)

        # Adjust pointers
        node.ref.ref = node
        node.ref = None

        return new_head

    # Helper function to initiate the recursive reverse
    def reverse_recursively(self):
        self.head = self.recursive_reverse(self.head)

    #reverse a LL using stack
    def reverse_using_stack(self):
        stack = []
        n = self.head
        while n is not None:
            stack.append(n.data)
            n = n.ref

        n = self.head
        while n is not None:
            n.data = stack.pop()
            n = n.ref

    def rotate(self, k):
        if self.head is None:
            print("Linked list is empty so can't rotate")
        #n - current node
        length, n = 1, self.head
        while n.ref is not None:
            n = n.ref
            length += 1
        
        k = k % length
        if k == 0:
            self.traverse()
        #moving to the pivot and rotating
        n = self.head
        for i in range(length - k -1):
            n = n.ref
        new_head = n.ref
        n.ref.ref.ref = self.head
        n.ref = None
        self.head = new_head
        
        

    
            
            
 

    
LL1 = LinkedList()
for i in range(6,0,-1):
    LL1.add_begin(i)
LL1.traverse()
#LL1.reverse()
#LL1.reverse_recursively()
#LL1.reverse_using_stack()
#LL1.traverse()
LL1.rotate(2)
LL1.traverse()





