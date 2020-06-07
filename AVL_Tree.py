class TreeNode(object):

    def __init__(self, val):
        super().__init__()
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):


    def insert(self, root, key):
        
        if not root:
            return TreeNode(key)
        elif root.val < key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)

        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if balance < -1 and key > root.right.val: 
            return self.left_rotate(root) 
        
        if balance < -1 and key < root.right.val: 
            root.right = self.right_rotate(root.right) 
            return self.left_rotate(root)

        return root 

    def delete(self, root, key):
        
        if root == None:
            return None
        
        if root.val < key:
            root.right = self.delete(root.right, key)
        elif root.val > key:
            root.left = self.delete(root.left, key)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            
            min_val = self.get_min_value_node(root.right)
            root.val = min_val.val
            root.right = self.delete(root.right, min_val.val)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right)) 
        
        balance = self.get_balance(root) 

        if balance > 1 and self.get_balance(root.left) >= 0: 
            return self.rightRotate(root) 

        if balance > 1 and self.get_balance(root.left) < 0: 
            root.left = self.left_rotate(root.left) 
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0: 
            return self.left_rotate(root)  

        if balance < -1 and key < root.right.val: 
            root.right = self.right_rotate(root.right) 
            return self.left_rotate(root) 
  
        return root

    def get_height(self, node:TreeNode) -> int:
        if not node:
            return 0

        return node.height 

    def get_balance(self, node:TreeNode) -> int:
        if not node:
            return 0
        
        return self.get_height(node.left) - self.get_height(node.right)
    
    def left_rotate(self, node):
        right_node = node.right
        T2 = right_node.left
        
        # Perform rotation
        node.right = T2
        right_node.left = node

        # Update height
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right_node.height = 1 + max(self.get_height(right_node.left),self.get_height(right_node.right))
        
        return right_node

    def right_rotate(self, node):
        
        left_node = node.left
        T3 = left_node.right

        # Perform rotation
        left_node.right = node
        node.left = T3

        # Update height
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left_node = 1 + max(self.get_height(left_node.left), self.get_height(left_node.right))

        return left_node
    

    def get_min_value_node(self, root): 
        if root is None or root.left is None: 
            return root 

        return self.get_min_value_node(root.left)