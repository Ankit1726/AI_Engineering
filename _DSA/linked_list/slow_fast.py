# ------------ Slow-Fast Approach ---------------
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

    # slow fast appraoch
    def find_mid(self):  # TC:O(n)
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next  # +1
            fast = fast.next.next  # +2

        return slow  # mid element

    def print_ll(self):
        temp = self.head
        while temp != None:
            print(f"{temp.val}->", end=" ")
            temp = temp.next
        print("null")


ll = LinkedList()

for e in [1, 2, 3, 4, 5]:
    ll.add_element(e)

print("Original Linked List")
ll.print_ll()
print(f"middle of linked list: {ll.find_mid().val}")
