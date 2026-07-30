## Creating Simple Binary Tree 
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


def print_nodes(root):
    if root is None:
        return
    
    print(root.val,end=" ")
    # recursion call
    print_nodes(root.left)
    print_nodes(root.right)
print_nodes(root)

# '''
#         1
#        / \
#       2   3
#      / \
#     4   5
# '''