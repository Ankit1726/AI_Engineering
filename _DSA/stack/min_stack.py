## ---------------- Design: Min Stack --------------------
class Stack:
    def __init__(self): # Tc:O(1) & SC:O(n)
        self.stack = []
        self.min_val = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val
            self.stack.append(val)
        else:
            if val < self.min_val:
                encoded_val = 2 * val - self.min_val
                self.stack.append(encoded_val)
                self.min_val = val
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return

        top = self.stack.pop()
        if top < self.min_val:
            # restore prevoius min value
            self.min_val = 2 * self.min_val - top

    def top(self) -> int:
        if not self.stack:
            return -1
        top = self.stack.pop()
        self.stack.append(top)

        if top < self.min_val:
            return self.min_val
        return top

    def getMin(self) -> int:
        return self.min_val


min_stack = Stack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print("Get Min:", min_stack.getMin())
min_stack.pop()
print("Top:", min_stack.top())
print("Get Min:", min_stack.getMin())