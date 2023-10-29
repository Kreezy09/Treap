import random

#treap node class
class TreapNode:
    def __init__(self,key):
        self.key = key
        self.priority = random.randint(0, 99)
        self.left = None
        self.right = None

#treap class
class Treap:
    def __init__(self):
        self.root = None

    #Right and left rotations
    def rightRotation(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def leftRotation(self, x):
        y = x.right 
        x.right = y.left   
        y.left = x
        return y

    def insert(self, current_node, key):
        if not current_node:
            return TreapNode(key)
        #Check if key is smaller than the current node
        if key <= current_node.key:
            current_node.left = self.insert(current_node.left, key)
            
            #Perform rotations to ensure priority is adhered to
            if current_node.left.priority > current_node.priority:
                current_node = self.rightRotation(current_node)
        else:
            current_node.right = self.insert(current_node.right, key)
            
            #Fix heap
            if current_node.right.priority > current_node.priority:
                current_node = self.leftRotation(current_node)
        return current_node

    def delete(self, current_node, key):
        if not current_node:
            return current_node
        
        if key < current_node.key:
            current_node.left = self.delete(current_node.left, key)
        elif key > current_node.key:
            current_node.right = self.delete(current_node.right, key)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            
            elif current_node.left.priority < current_node.right.priority:
                current_node = self.leftRotation(current_node)
                current_node.left = self.delete(current_node.left, key)
            else:
                current_node = self.rightRotation(current_node)
                current_node.right = self.delete(current_node.right, key)
        return current_node

    def search(self, current_node, key):
        if not current_node or current_node.key == key:
            return current_node
        
        if key < current_node.key:
            return self.search(current_node.left, key)
        
        return self.search(current_node.right, key)

    def inorder(self, current_node):
        if current_node:
            self.inorder(current_node.left) #Recur on left subtree
            print("Key: ", current_node.key, "Priority: ", current_node.priority)
            self.inorder(current_node.right) # REcur on right subtree
        
    def preorder(self, current_node):
        if current_node:
            print("Key: ", current_node.key, "Priority: ", current_node.priority)
            self.preorder(current_node.left)  # Recur on left subtree
            self.preorder(current_node.right)  # Recur on right subtree
            
    def postorder(self, current_node):
        if current_node:
            self.postorder(current_node.left)  # Recur on left subtree
            self.postorder(current_node.right)  # Recur on right subtree
            print("Key: ", current_node.key, "Priority: ", current_node.priority)

            
    
if __name__ == '__main__':
    treap = Treap()
        # Insert nodes into the treap
    treap.root = treap.insert(treap.root, 50)
    treap.root = treap.insert(treap.root, 30)
    treap.root = treap.insert(treap.root, 20)
    treap.root = treap.insert(treap.root, 40)
    treap.root = treap.insert(treap.root, 70)
    treap.root = treap.insert(treap.root, 60)
    treap.root = treap.insert(treap.root, 80)
    
    print("Inorder traversal:")
    treap.inorder(treap.root)
    
    print("Preorder travesal:")
    treap.preorder(treap.root)
    
    print("Postorder traversal:")
    treap.postorder(treap.root)

    # Search for a node in the treap
    key = int(input("Enter key: "))
    search_result = treap.search(treap.root, key)
    if search_result:
        print(f"Node with key {key} found in the treap.")
    else:
        print(f"Node with key {key} not found in the treap.")
    
    # Delete a node from the treap
    key_to_delete = 30
    treap.root = treap.delete(treap.root, key_to_delete)
    print(f"Deleted node with key {key_to_delete}.")
    
    # Print the treap after deletion
    print("Inorder traversal of the modified treap:")
    treap.inorder(treap.root)