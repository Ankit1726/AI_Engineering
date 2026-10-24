## --------------- Stack Using List ---------------
class Stack_List:
    def __init__(self):
        self.stack = []

    def is_empty(self):  # O(1)
        return len(self.stack) == 0

    def push(self, val):  # O(1)
        self.stack.append(val)

    def pop(self):  # O(1)
        if self.is_empty():
            raise IndexError("Empty stack...")
        return self.stack.pop()

    def top(self):  # O(1)
        if self.is_empty():
            raise IndexError("Top can not determined due to emptyness...")
        return self.stack[-1]

    def display(self):
        print(self.stack)


s = Stack_List()

# push elements
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("Stack elements:", s.stack)
print("Top element:", s.top())

print("Popped:", s.pop())
print("Stack after pop:", s.stack)