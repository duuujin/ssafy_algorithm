class Node:
    def __init__(self, key):
        self.key = key  
        self.left = None  
        self.right = None  

class BST:
    def __init__(self):
        self.root = None  

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)  
        else:
            self._insert(self.root, key) 

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)  
            else:
                self._insert(node.left, key) 
        else:
            if node.right is None:
                node.right = Node(key) 
            else:
                self._insert(node.right, key)  

    def delete(self, key):
        self.root = self._delete(self.root, key) 

    def _delete(self, node, key):
        if node is None:
            return node  

        if key < node.key:
            node.left = self._delete(node.left, key)  
        elif key > node.key:
            node.right = self._delete(node.right, key)  
        else:
            if node.left is None:
                return node.right  
            elif node.right is None:
                return node.left  

            temp = self._minValueNode(node.right)  
            node.key = temp.key 
            node.right = self._delete(node.right, temp.key) 

        return node

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left  
        return current

    def search(self, key):
        return self._search(self.root, key)  

    def _search(self, node, key):
        if node is None or node.key == key:
            return node 
        if key < node.key:
            return self._search(node.left, key)  
        return self._search(node.right, key) 

    def inorder(self):
        self._inorder(self.root) 
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)  
            print(node.key, end=' ') 
            self._inorder(node.right) 

# BST 생성
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)

bst.inorder()
