## --------------- LRU Cache Problem -----------------
class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Map to store key -> Node reference

        # Dummy head and tail nodes to avoid edge cases
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _del_Node(self, oldNode: Node):
        """Corresponds to the delNode(oldNode) logic on the board."""
        oldPrev = oldNode.prev
        oldNext = oldNode.next

        # Re-establish pointers to bypass oldNode
        oldPrev.next = oldNext
        oldNext.prev = oldPrev

    def _add_Node(self, newNode: Node):
        """Inserts a new node right after the dummy head (Most Recently Used)."""
        oldNext = self.head.next

        # Connect head to newNode
        self.head.next = newNode
        newNode.prev = self.head

        # Connect newNode to oldNext
        newNode.next = oldNext
        oldNext.prev = newNode

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Fetch node, remove it from current position, and move to front
        node = self.cache[key]
        self._del_Node(node)
        self._add_Node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # 1. If key already exists, delete old node and erase from map
        if key in self.cache:
            oldNode = self.cache[key]
            self._del_Node(oldNode)
            del self.cache[key]

        # 2. If capacity reached, remove the least recently used item (tail.prev)
        elif len(self.cache) == self.capacity:
            lru_node = self.tail.prev
            del self.cache[lru_node.key]
            self._del_Node(lru_node)

        # 3. Create new node, add it to DLL, and store in map
        newNode = Node(key, value)
        self._add_Node(newNode)
        self.cache[key] = newNode


lru = LRUCache(2)

lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))

lru.put(3, 3)
print(lru.get(2))

lru.put(4, 4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))