class Node:
    def __init__(self, val: int, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class LinkedList:
    def __init__(self):
        self.fhead = None

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None

        node_map = {}

        # Pass 1: Copy nodes from old -> new without linking pointers
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: Connect next and random pointers using map lookup
        curr = head
        while curr:
            copied_node = node_map[curr]
            copied_node.next = node_map.get(curr.next, None)
            copied_node.random = node_map.get(curr.random, None)
            curr = curr.next

        return node_map[head]


# --- Driver Code ---
ll = LinkedList()

# Creating list: 7 -> 13 -> 11
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)

node1.next = node2
node2.next = node3

node1.random = None
node2.random = node1
node3.random = node2

cloned_head = ll.copyRandomList(node1)

# Verification
print("Original head val:", node1.val, "| Cloned head val:", cloned_head.val)
print("Original head is Cloned head ?", node1 is cloned_head)
print("Cloned node2 random val:", cloned_head.next.random.val)
