# ------------ Circular Linked List ---------------
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Circular_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at head O(1)
    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            new_node.next = self.head
            return

        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head  # maintain cycle

    # Insert at tail O(1)
    def insert_at_tail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            new_node.next = self.head
            return

        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head  # Maintain circular link

    # Delete Head Node - O(1)
    def delete_at_head(self):
        if not self.head:
            print("List is empty")
            return

        # Single node case
        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next
        self.tail.next = self.head

    # Delete Tail Node - O(N)
    def delete_at_tail(self):
        if not self.head:
            print("List is empty")
            return

        # Single node case
        if self.head == self.tail:
            self.head = self.tail = None
            return

        # Traverse to the second last node
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next

        curr.next = self.head
        self.tail = curr

    # Display / Print List
    def print_list(self):
        if not self.head:
            print("List is empty")
            return

        curr = self.head
        print("CLL: ", end="")
        while True:
            print(curr.val, end=" -> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(head)")

cll = Circular_LinkedList()

# Insertion
cll.insert_at_tail(10)
cll.insert_at_tail(20)
cll.insert_at_tail(30)
cll.insert_at_head(5)
cll.print_list()

cll.delete_at_head()
cll.print_list()

cll.delete_at_tail()
cll.print_list()