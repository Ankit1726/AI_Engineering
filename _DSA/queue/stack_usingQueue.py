## ------------------ Implement Stack Using Queue --------------------
from collections import deque


class Queue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def empty(self) -> bool:
        return not self.q1

    def push(self, x: int) -> None:  # TC:O(n)
        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Push new element to q1
        self.q1.append(x)

        # Move everything back to q1
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        return self.q1.popleft()

    def front(self) -> int:
        return self.q1[0]

    def display(self):
        return f"Queue (Front --> Rear):{self.q1}"


q = Queue()
q.push(10)
q.push(20)
q.push(30)

print(q.display())
print(f"Queue Front:{q.front()}")
print(f"Queue Pop:{q.pop()}")
print(f"Is Empty Queue:{q.empty()}")
print(q.display())