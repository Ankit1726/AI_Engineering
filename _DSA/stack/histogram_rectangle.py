## ------------- Largest Rectangle In Histogram ---------------
class Stack:  # TC:O(n) & SC:O(n)
    def largest_rectangle(self, ht: list[int]) -> int:
        n = len(ht)
        left_small = [0] * n
        right_small = [0] * n
        stack = []

        # find prevoius smaller (left boundary)
        for i in range(n):
            while stack and ht[stack[-1]] >= ht[i]:
                stack.pop()
            left_small[i] = stack[-1] if stack else -1
            stack.append(i)

        # clear stack for reused
        stack.clear()

        # find next smaller (right boundary)
        for i in range(n - 1, -1, -1):
            while stack and ht[stack[-1]] >= ht[i]:
                stack.pop()
            right_small[i] = stack[-1] if stack else n
            stack.append(i)

        # calculate maximum area
        max_area = 0
        for i in range(n):
            height = ht[i]
            width = right_small[i] - left_small[i] - 1
            current_area = height * width
            max_area = max(max_area, current_area)
        return max_area


s = Stack()
ht = [2, 1, 5, 6, 2, 3]
print(f"Maximum Area Of Rectangle: {s.largest_rectangle(ht)}")