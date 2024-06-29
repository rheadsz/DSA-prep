class BST:
    def __init__(self,key):
        self.key = key      #key is the root node
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:    #if root node is empty/tree is empty
            self.key = data
            return

        if self.key == data:       #ignore if its a duplicate node
            return 

        if data < self.key:     #if data < root
            if self.lchild:     #if root has  a left child
                self.lchild.insert(data)    #recursion 
            else:
                self.lchild = BST(data)     #if root has no left child then make data as the left child
        else:   #if data is > root
            if self.rchild: #if root has a right child
                self.rchild.insert(data)    #recursion on right node
            else:
                self.rchild = BST(data)     #if there's no right child then make data as right child

    def search(self,data):
        if self.key == data:
            print(str(data)+" found and is present in the tree")
            return
        if data < self.key: #if data < root node
            if self.lchild: #if root has lchild
                self.lchild.search(data)
            else:
                print("Node not in the tree")
        else:   #if data > root
            if self.rchild: #if root has rchild
                self.rchild.search(data)
            else:
                print("Node not in the tree")

    def preorder(self): #root - lchild -  rchild
        print(self.key,end=" ")

        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self): #lchild - root  - rchild
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self): #lchild - rchild - root
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")

    def delete(self, data, curr):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("Node is not in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("Node is not in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr)
        return self

    def count(node):
        if node is None:
            return 0
        return 1+count(node.lchild)+count(node.rchild)

    def min_node(self):
        current = self  #now current becomes the root node
        while current.lchild:
            current = current.lchild
        print("The smallest node is "+str(current.key))

    
    def max_node(self):
        current = self  #now current becomes the root node
        while current.rchild:
            current = current.rchild
        print("The smallest node is "+str(current.key))



            


root = BST(None)

nodes = [10,5, 17, 23, 16, 11, 21, 30, 3]
for node in nodes:
    root.insert(node)
root.search(23)
print("Preorder")
root.preorder()
print()
print("Inorder")
root.inorder()
print()
print("Postorder")
root.postorder()
#root.delete(10, root.key) #root.key is also passed here to check if we are deleting the root node or not
print()
#print("After deletion")

#root.preorder()
root.min_node()
root.max_node()