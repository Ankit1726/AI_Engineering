# -------------- Detect & Remove Cycle In Linked List --------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_item(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.val}->", end=" ")
            temp = temp.next
        print("null")

    # Detect & Remove Cycle
    def detect_and_remove_cycle(self):
        slow = self.head
        fast = self.head

        cycle_exists = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Meet point
            if slow == fast:
                cycle_exists = True
                break

        if not cycle_exists:
            print("No cycle detected..!")
            return False

        # Find start node of cycle and remove cycle
        slow = self.head

        # Case 1: Cycle starts at the head node
        if slow == fast:
            while fast.next != slow:
                fast = fast.next
            fast.next = None  # Remove cycle
        else:
            # Case 2: Cycle starts somewhere inside the list
            prev = None
            while slow != fast:
                slow = slow.next
                prev = fast
                fast = fast.next
            # Break the cycle link
            prev.next = None

        print("Cycle successfully removed..!")
        return True

ll = LinkedList()

for i in range(1, 6):
    ll.add_item(i)

print("--- Initial Linked List ---")
ll.print_ll()

# Creating a cycle manually: 5 -> 3
# 1 -> 2 -> 3 -> 4 -> 5
#           ^         |
#           |_________|

node3 = ll.head.next.next  # Node with value 3
node5 = ll.head.next.next.next.next  # Node with value 5
node5.next = node3  # Creates cycle: 5 -> 3

print("\n--- Running Detection & Removal ---")
ll.detect_and_remove_cycle()

print("\n--- After Removing Cycle ---")
ll.print_ll()