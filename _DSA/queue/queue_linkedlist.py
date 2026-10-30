## ----------------- Queue Using Linked List -------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):  # TC:O(1)
        return self.head is None

    def push(self, data):  # TC:O(1)
        new_node = Node(data)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):  # TC:O(1)
        if self.is_empty():
            print("Queue is empty..!")
            return -1

        popped_data = self.head.data  # front = head --> pop item
        self.head = self.head.next  # +1

        if self.head is None:
            self.tail = None
        return popped_data

    def front(self):  # TC:O(1)
        if self.is_empty():
            return -1
        return self.head.data

    def display(self):  # TC:O(n)
        if self.is_empty():
            return -1

        curr = self.head
        print("Queue Item:(Front --> Rear)")
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("null")


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)

q.display()
print(f"front item:{q.front()}")
print(f"popped item:{q.pop()}")