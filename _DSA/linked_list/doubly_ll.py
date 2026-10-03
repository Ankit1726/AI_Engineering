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

    
dll = Doubly_LL()
dll.push_front(10)
dll.push_front(20)
dll.push_front(30)
dll.push_back(40)
dll.push_back(50)
dll.print_forward()
dll.print_backward()