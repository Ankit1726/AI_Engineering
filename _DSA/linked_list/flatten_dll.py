# ------------ Flatten Doubly Linked List --------------
class Node:
    def __init__(self, data):
        self.data = data
        self.child = None
        self.next = None
        self.prev = None


class Doubly_LinkedList:
    def flatten_dll(self, head): # TC:O(N) & SC:O(D)
        if not head:
            return None
        curr = head
        while curr:
            # If current node has a valid child node
            if curr.child:
                next_node = curr.next

                # Recursively flatten child branch
                child_head = self.flatten_dll(curr.child)

                # Connect child <--> curr
                curr.next = child_head
                child_head.prev = curr
                curr.child = None

                # Find tail of child list
                child_tail = child_head
                while child_tail.next:
                    child_tail = child_tail.next

                # Connect child tail <--> next node
                if next_node:
                    child_tail.next = next_node
                    next_node.prev = child_tail

            curr = curr.next
        return head

    def print_dll(self, head):
        curr = head
        vals = []
        while curr:
            vals.append(str(curr.data))
            curr = curr.next
        print(" <--> ".join(vals) + " <--> null")


# Constructing structure:
# 1 <-> 2 <-> 3 <-> 4 <-> 5
#               |
#               6 <-> 7 <-> 8
#                     |
#                     9 <-> 10

n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
n6, n7, n8 = Node(6), Node(7), Node(8)
n9, n10 = Node(9), Node(10)

# Top level: 1 <-> 2 <-> 3 <-> 4 <-> 5
n1.next, n2.prev = n2, n1
n2.next, n3.prev = n3, n2
n3.next, n4.prev = n4, n3
n4.next, n5.prev = n5, n4

# Middle level: 6 <-> 7 <-> 8
n6.next, n7.prev = n7, n6
n7.next, n8.prev = n8, n7
n3.child = n6

# Bottom level: 9 <-> 10
n9.next, n10.prev = n10, n9
n7.child = n9

# Execution
dll = Doubly_LinkedList()
flatten_head = dll.flatten_dll(n1)
dll.print_dll(flatten_head)