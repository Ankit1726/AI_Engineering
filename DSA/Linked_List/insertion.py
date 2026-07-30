class Node:
     def __init__(self, val):
          self.val = val 
          self.next = None 

class LL_Insertion:
     def __init__(self):
          self.head = None 

     # 1. Insertion at the beginning
     def insert_begin(self, val):
          new_node = Node(val)
          new_node.next = self.head
          self.head = new_node 
          
     # 2. Insertion at the end
     def insert_end(self, val):
          new_node = Node(val)
          if self.head is None:
               self.head = new_node  
               return

          curr = self.head
          while curr.next is not None:
               curr = curr.next 
          curr.next = new_node

     # 3. Insertion at any 1-based index position 
     def insert_pos(self, val, pos):
          new_node = Node(val)
          
          if pos == 1:
               new_node.next = self.head
               self.head = new_node 
               return
               
          curr = self.head 
          for i in range(1, pos - 1): 
               if curr is None:
                    print("invalid position")
                    return 
               curr = curr.next 

          # Check if the position is completely out of bounds
          if curr is None:
               print("invalid position")
               return
   
          new_node.next = curr.next 
          curr.next = new_node

     # 4. Display linked list 
     def print_ll(self):
          curr = self.head 
          while curr is not None:
               print(curr.val, end=" -> ")
               curr = curr.next 
          print("None")


# --- Testing the corrected implementation ---
ll = LL_Insertion()

# Test inserting at the beginning
ll.insert_begin(10)
ll.insert_begin(20)
ll.insert_begin(30)
print("After insert_begin (30, 20, 10):")
ll.print_ll() 

# Test inserting at the end
ll.insert_end(40)
print("\nAfter insert_end (40):")
ll.print_ll()

# Test inserting at position 3 (between 20 and 10)
ll.insert_pos(25, 3)
print("\nAfter insert_pos (25 at position 3):")
ll.print_ll()