# ---------- Reverse Nodes in K-Group ------------ 
class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

class LinkedList:
    def reverse_KGroup(self, head: Node, k: int) -> Node:
        # Step 1: Check if k nodes exist ahead
        temp = head
        count = 0
        while temp and count < k:
            temp = temp.next 
            count += 1 

        # If remaining nodes are less than k, leave them as is
        if count < k:
            return head 

        # Step 2: Reverse first k nodes
        prev = None 
        curr = head 
        next_node = None 
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Recursive call for remaining nodes
        head.next = self.reverse_KGroup(curr, k)
        return prev 

    def print_list(self, head: Node):
        vals = []
        curr = head
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(vals) + " -> null")


# Helper function to create linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

ll = LinkedList()
head = create_linked_list([1, 2, 3, 4, 5])
print("Original List:")
ll.print_list(head)


k = 2
new_head = ll.reverse_KGroup(head, k)

print(f"\nList after reversing in groups of {k}:")
ll.print_list(new_head)