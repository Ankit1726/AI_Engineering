## Remove Duplicates From Sorted Linked List 
class Node:
     def __init__(self,val):
          self.val = val 
          self.next = None 

class Solution:
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

     def print_ll(self):
          curr = self.head 
          while curr is not None:
               print(curr.val,end=" -> ")
               curr = curr.next 
          print("None")

     def remove_dup(self):
          if not self.head or not self.head.next:
               return self.head 

          slow = self.head 
          fast = self.head.next

          while fast:
               if(slow.val == fast.val):
                    slow.next = fast.next 
               else:
                    slow = slow.next 
               fast = fast.next 
          return self.head 
     
     
ll = Solution()
ll.add_node(1)
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(3)
ll.print_ll()

ll.remove_dup()
ll.print_ll()