## Level Order Traversal
from  collections import deque

class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def level_order(root):
    if root is None:return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val,end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(root.right)

level_order(root)