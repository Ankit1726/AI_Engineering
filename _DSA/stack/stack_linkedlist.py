## --------------- Stack Using Linked List -------------- 
class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None 

class Stack_LinkedList:
    def __init__(self):
        self.head = None 
        self.size = 0

    def is_empty(self): # O(1)
        return self.head is None 
    
    def push(self,val): # O(1)
        new_node = Node(val)
        new_node.next = self.head 
        self.head = new_node # insert at top 
        self.size += 1

    def pop(self): # O(1)
        if self.is_empty():
            raise IndexError("Empty stack...")
        pop_data = self.head.val 
        self.head = self.head.next # del from head 
        self.size -= 1 
        return pop_data

    def top(self): # O(1)
        if self.is_empty():
            raise IndexError("Empty stack...")
        return self.head.val

    def display(self): # O(n)
        curr = self.head 
        items = []
        while curr:
            items.append(curr.val)
            curr = curr.next # +1 increase 
        print("Stack (Top To Bottom):",items)

s = Stack_LinkedList()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.display()

print(f"Deleted Element:{s.pop()}")
s.display()

print(f"Top Element:{s.top()}")