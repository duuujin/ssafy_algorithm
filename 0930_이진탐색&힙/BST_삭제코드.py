class Node:
    def __init__(self, key):
        self.key = key  
        self.left = None  
        self.right = None

class BST:
    def __init__(self):
        self.root = None  

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
