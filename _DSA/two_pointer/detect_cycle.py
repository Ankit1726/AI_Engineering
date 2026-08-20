## Detect Cycle In LinkedList 
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow,fast = head,head 

    while fast and fast.next:
        slow = slow.next  # +1
        fast = fast.next.next   # +2

        if(slow == fast):
            return True
    return False

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_2
print("Has Cycle:", has_cycle(node_1))