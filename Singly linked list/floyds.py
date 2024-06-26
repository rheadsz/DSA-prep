class  Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def findMid(self):
        #add items to LL
        for i in range(0,4):
            new_node = Node(i)
            new_node.ref = self.head
            self.head = new_node


        fast_ptr = self.head
        slow_ptr = self.head

        while fast_ptr is not None and fast_ptr.ref is not None:
            slow_ptr = slow_ptr.ref
            fast_ptr = fast_ptr.ref.ref

        return slow_ptr.data

LL4 = LinkedList()
LL4.findMid()