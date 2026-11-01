## ---------------------- Implement Queue Using Stack -----------------------
from collections import deque

class Stack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def empty(self) -> bool:
        return not self.s1

    def push(self, x: int) -> None:  # TC:O(n)
        # Move all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # Push new element to s1
        self.s1.append(x)

        # Move everything back to s1
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def display(self):
        return self.s1


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.display())
print(f"Popped Item:{s.pop()}")
print(f"Peek Item:{s.peek()}")
print(s.display())