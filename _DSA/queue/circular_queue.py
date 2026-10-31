## ------------------ Circular Queue ----------------------
class CicularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.front = 0
        self.rear = -1
        self.queue = [None] * capacity

    def is_empty(self) -> bool:  # TC:O(1)
        return self.curr_size == 0

    def is_full(self) -> bool:  # TC:O(1)
        return self.curr_size == self.capacity

    def push(self, val: int) -> bool:  # TC:O(1)
        if self.is_full():
            print("Circular Queue Full..!")
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = val
        self.curr_size += 1
        return True

    def pop(self) -> int:  # TC:O(1)
        if self.is_empty():
            return -1

        popped_data = self.queue[self.front]
        self.queue[self.front] = None

        self.front = (self.front + 1) % self.capacity
        self.curr_size -= 1
        return popped_data

    def get_front(self) -> int:  # TC:O(1)
        if self.is_empty():
            return -1
        return self.queue[self.front]


cq = CicularQueue(capacity=4)
cq.push(1)
cq.push(2)
cq.push(3)
cq.push(4)

print("Front element:", cq.get_front())
print("Popped:", cq.pop())
cq.push(5)
print("New Front Element:", cq.get_front())