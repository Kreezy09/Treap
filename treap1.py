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
def rightRotation(y):
    x = y.left
    B = x.right
    
    x.right = y
    y.left = B
    return x

def leftRotation(x):
    y = x.right
    B = y.left
    
    y.left = x
    x.right = B
    return y

def insert(current_node, key):
    if not current_node:
        return TreapNode(key)
    #Check if key is smaller than the current node
    if key <= current_node.key:
        current_node.left = insert(current_node.left, key)
        
        #Perform rotations to ensure priority is adhered to
        if current_node.left.priority > current_node.priority:
            current_node = rightRotation(current_node)
            
    
    