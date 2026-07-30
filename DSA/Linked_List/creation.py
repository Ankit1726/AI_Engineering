class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list
        self.head = None 

    # Add node to the end of the list
    def add_node(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next 
            curr.next = new_node

    # Iterative display method
    def display_node(self):
        curr = self.head 
        while curr is not None:
            print(curr.val, end=" -> ")
            curr = curr.next 
        print("None") 

    # Recursive display method
    def display_rec(self, head):
        if head is None:
            return
        print(head.val, end=" -> ")
        self.display_rec(head.next)

     # find length of liked list 
    def find_length(self):
        len = 0 
        curr = self.head
        while curr is not None:
          len+=1
          curr = curr.next
        return len
          
        

# --- Testing the Implementation ---
ll = LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)

print("Iterative Display:")
ll.display_node()

print("\Recursive Display:")
ll.display_rec(ll.head)
print("None")

print(f"Length of the linked list:{ll.find_length()}")