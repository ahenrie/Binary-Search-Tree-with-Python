class Node:
    def __init__(self, data, count = 1):
        self.data = data
        self.right = None
        self.left = None
        self.count = count

class BST:
    def __init__(self):
        self.root = None
    
    def size(self):
        return self._size_recursively(self.root)
    
    def _size_recursively(self, node):
        if node is None:
            return 0
        return 1 + self._size_recursively(node.left) + self._size_recursively(node.right)
    
    def is_empty(self):
        return self.root is None
    
    def height(self):
        return self._height_recursively(self.root)
    
    def _height_recursively(self, node):
        if node is None:
            return -1
        return 1 + max(self._height_recursively(node.left), self._height_recursively(node.right))

    def add(self, pair):
        if self.root is None:
            self.root = Node(pair)
        else:
            current_node = self.root
            while current_node is not None:
                if pair.letter < current_node.data.letter:
                    if current_node.left is None:
                        current_node.left = Node(pair)
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = Node(pair)
                        current_node = None
                    else:
                        current_node = current_node.right
        return self

    def inorder(self):
        result = []
        self._inorder_recursively(self.root, result)
        return result
    
    def _inorder_recursively(self, node, result):
        if node:
            self._inorder_recursively(node.left, result)
            result.append(node.data)
            self._inorder_recursively(node.right, result)

    def preorder(self):
        result = []
        self._preorder_recursively(self.root, result)
        return result
    
    def _preorder_recursively(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_recursively(node.left, result)
            self._preorder_recursively(node.right, result)
    
    def postorder(self):
        result = []
        self._postorder_recursively(self.root, result)
        return result
    
    def _postorder_recursively(self, node, result):
        if node is not None:
            self._postorder_recursively(node.left, result)
            self._postorder_recursively(node.right, result)
            result.append(node.data)

    def find(self, pair):
        current_node = self.root
        while current_node is not None:
            if current_node.data == pair:
                return current_node
            elif pair.letter < current_node.data.letter:
                current_node = current_node.left
            else:
                current_node = current_node.right
        raise ValueError("item not in tree")
    
    
    def remove(self, key):
        parent = None
        current_node = self.root
        
        # Search for the node.
        while current_node is not None:
            # Check if current_node has a matching key.
            if current_node.data == key: 
                if current_node.left is None and current_node.right is None:   # Case 1
                    if parent is None: # Node is root
                        self.root = None
                    elif parent.left is current_node: 
                        parent.left = None
                    else:
                        parent.right = None
                    return  # Node found and removed
                elif current_node.left is not None and current_node.right is None:  # Case 2
                    if parent is None: # Node is root
                        self.root = current_node.left
                    elif parent.left is current_node: 
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return  # Node found and removed
                elif current_node.left is None and current_node.right is not None:  # Case 2
                    if parent is None: # Node is root
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return  # Node found and removed
                else:                                    # Case 3
                    # Find successor (leftmost child of right subtree)
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left
                    current_node.data = successor.data      # Copy successor to current node
                    parent = current_node
                    current_node = current_node.right       # Remove successor from right subtree
                    key = parent.data                        # Loop continues with new key
            elif current_node.data < key: # Search right
                parent = current_node
                current_node = current_node.right
            else:                          # Search left
                parent = current_node
                current_node = current_node.left
            
        return # Node not found
