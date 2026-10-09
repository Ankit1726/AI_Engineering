# ------------- Swap Nodes In Pairs


class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def swapPairs(self, head: Node) -> Node:
        # Dummy node to handle edge cases easily
        dummy = Node(0)
        dummy.next = head
        prev = dummy

        # Loop as long as there is a pair of nodes to swap
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # Swapping links
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev pointer two nodes ahead for the next pair
            prev = first
        return dummy.next

    # Utility functions defined as static methods
    @staticmethod
    def create_linked_list(arr):
        dummy = Node(0)
        curr = dummy
        for val in arr:
            curr.next = Node(val)
            curr = curr.next
        return dummy.next

    @staticmethod
    def print_linked_list(head):
        elements = []
        curr = head
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(elements) if elements else "null")


ll = LinkedList()
arr = [1, 2, 3, 4]
head = ll.create_linked_list(arr)

print("Original List:")
ll.print_linked_list(head)

swapped_head = ll.swapPairs(head)
print("Swapped List:")
ll.print_linked_list(swapped_head)