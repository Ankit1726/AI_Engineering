class Node:
     def __init__(self, val):
          self.val = val 
          self.next = None 

class LL_Deletion:
     def __init__(self):
          self.head = None 

     def add_node(self, val):
             new_node = Node(val)
             if self.head is None:
                 self.head = new_node
             else:
                 curr = self.head
                 while curr.next is not None:
                     curr = curr.next 
                 curr.next = new_node

     def del_start(self):
          if self.head is None:
               print("empty lisked list")
               return None 
          new_head = self.head.next 
          self.head.next = None 
          self.head = new_head
          return new_head

     def del_end(self):
          if self.head is None:
               print("empty linked list")
               return None 

          if self.head.next is None: 
               return None

          curr = self.head
          while curr.next.next is not None:
               curr = curr.next 
          curr.next = None 
          return self.head

     def del_pos(self,val):
          if self.head is None:
               print("empty linked list")
               return None 
          if self.head.val == val:
               new_head = self.head.next 
               self.head.next = None 
               return new_head
          
          curr = self.head
          while curr.next is not None and curr.next.val!=val:
               curr = curr.next
          if curr.next is None:
               print("value not found")
               return self.head

          temp = curr.next 
          curr.next = curr.next.next
          temp.next = None 
          return self.head

     
     def print_ll(self):
          curr = self.head 
          while curr is not None:
               print(curr.val, end=" -> ")
               curr = curr.next 
          print("None")

ll = LL_Deletion()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)
ll.add_node(300)
ll.add_node(50)
ll.print_ll()

ll.del_start()
ll.print_ll()

ll.del_end()
ll.print_ll()

ll.del_pos(300)
ll.print_ll()