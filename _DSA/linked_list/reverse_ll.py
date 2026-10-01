# ------------ Reversed Linked List ----------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def reverse_ll(self): # TC:O(n)
        prev = None
        curr = self.head

        while curr:
            # save next node
            next_node = curr.next
            # reverse pointer
            curr.next = prev
            # move prev pointer to forward
            prev = curr
            # move curr pointer to forward
            curr = next_node

        self.head = prev  # update head
        return prev

    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.val}->", end=" ")
            temp = temp.next
        print("null")

ll = LinkedList()

# add element 
for e in [1,2,3,4,5]:
    ll.add_element(e)

print("Original Linked List")
ll.print_ll()

print("Reversed Linked List")
ll.reverse_ll()
ll.print_ll()