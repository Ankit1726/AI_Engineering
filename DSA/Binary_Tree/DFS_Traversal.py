## DFS Traversal (inorder | preorder | postorder)

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



# Preorder Traversal 
def pre_order(root):
    if root is None:
        return
    print(root.val,end=" ")
    pre_order(root.left)
    pre_order(root.right)

print("------- Preorder Traversal--------")
pre_order(root)
print()

# Inoreder Traversal
def in_oreder(root):
    if root is None:
        return
    in_oreder(root.left)
    print(root.val,end=" ")
    in_oreder(root.right)

print("------- Inorder Traversal--------")
in_oreder(root)

# Postorder Traversal 
def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val,end=" ")
print()
print("------- Postorder Traversal--------")
post_order(root)