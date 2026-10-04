# -------------- Doubly Linked List Implemtation ----------------
class Node:
    def __init__(self,val:int):
        self.val = val 
        self.next = None 
        self.prev = None 

class Doubly_LL:
    def __init__(self):
        self.head = None 
        self.tail = None 

    # push_front: (insert at start)
    def push_front(self,val:int):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Print List Forward 
    def print_forward(self):
        curr = self.head 
        print("Forward Print: ",end="")
        while curr:
            print(curr.val,end=" <-> ")
            curr = curr.next 
        print("null")

    # push_back: (insert at end)
    def push_back(self,val:int):
        new_node = Node(val)
        if not self.tail:
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # Print List Backward
    def print_backward(self):
        curr = self.tail
        print("Backward Print: ",end="")
        while curr:
            print(curr.val,end=" <-> ")
            curr = curr.prev
        print("null")

    # pop front: (delete from front)
    def pop_front(self):
        if not self.head:
            print("list is already empty")
            return

        temp = self.head 
        self.head = self.head.next 
        if self.head:
            self.head.prev = None # prev --> null
        else:
            self.tail = None 

        temp.next = None 
        del temp 

    # pop back: (delete from back)
    def pop_back(self):
        if not self.tail:
            print("list is empty")
            return

        temp = self.tail 
        self.tail = self.tail.prev # step back 

        if self.tail:
            self.tail.next = None 
        else:
            self.head = None # having only 1 node 

        temp.prev = None 
        del temp

dll = Doubly_LL()
dll.push_front(10)
dll.push_front(20)
dll.push_front(30)
dll.push_back(40)
dll.push_back(50)
dll.print_forward()
dll.print_backward()

dll.pop_front()
dll.print_forward()
dll.pop_back()
dll.print_backward()