# --------------- Merge 2 Sorted LinkedList --------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def build_list(self, arr):
        dummy = Node(-1)
        curr = dummy
        for val in arr:
            curr.next = Node(val)
            curr = curr.next
        return dummy.next

    def print_ll(self, head):
        temp = head
        while temp is not None:
            print(f"{temp.val}->", end=" ")
            temp = temp.next
        print("null")

    # Recursive Merge Function
    def mergelist_recursive(self, h1: Node, h2: Node) -> Node:
        if not h1:
            return h2
        if not h2:
            return h1

        if h1.val <= h2.val:
            h1.next = self.mergelist_recursive(h1.next, h2)
            return h1
        else:
            h2.next = self.mergelist_recursive(h1, h2.next)
            return h2


ll = LinkedList()

list1 = ll.build_list([1, 2, 3])
list2 = ll.build_list([4, 5, 6])

print("--- List 1 ---")
ll.print_ll(list1)

print("--- List 2 ---")
ll.print_ll(list2)

print("--- Merged List ---")
merged_list = ll.mergelist_recursive(list1, list2)
ll.print_ll(merged_list)