# ------------- Linked List Scratch Implementation ---------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    # push front (insert at front)
    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:  # head  -> null
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    # pusg back (insert at end)
    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    # pop front (delete at front)
    def pop_front(self):
        if self.head is None:
            print("linked list is empty..!")
            return
        temp = self.head
        self.head = self.head.next  # head move +1 step
        temp.next = None  # temp --> null (break connection)

    # pop back (delete at end)
    def pop_back(self):
        if self.head is None:
            print("linked list is empty..!")
            return

        temp = self.head
        while temp.next != self.tail:
            temp = temp.next  # +1

        temp.next = None
        self.tail = temp

    # insert at specific index value
    def insert(self, data, idx):
        if idx < 0:
            print("invalid index..!")
            return

        if idx == 0:
            self.push_front(data)
            return

        temp = self.head
        for _ in range(idx - 1):
            if temp is None:
                print("out of bound index..!")
                return
            temp = temp.next

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # search in linked list
    def search(self, key):
        temp = self.head
        idx = 0

        while temp is not None:
            # key found
            if temp.data == key:
                return idx
            temp = temp.next  # +1
            idx += 1
        return -1  # not found

    # print linked list
    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data}->", end=" ")
            temp = temp.next
        print("null")


ll = Linked_List()
ll.push_front(1)
ll.push_front(2)
ll.push_front(5)
ll.push_back(3)
ll.push_back(4)
ll.print_ll()
print(f"found at idx: {ll.search(2)}")

ll.pop_front()
ll.pop_back()
ll.print_ll()

ll.insert(7, 3)
ll.print_ll()