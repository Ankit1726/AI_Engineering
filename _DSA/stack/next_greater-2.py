## -------------- Next Greater-2 ----------------
class Stack:  # TC:O(n) & SC:O(n)
    def nextGreater(self, arr: list[int]) -> list[int]:
        n = len(arr)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            curr_idx = i % n

            # pop item: stack[i]<=curr[i]
            while stack and arr[stack[-1]] <= arr[curr_idx]:
                stack.pop()

            # stack item --> top element(next greater)
            if stack:
                res[curr_idx] = arr[stack[-1]]

            stack.append(curr_idx)
        return res


s = Stack()
arr = [1, 2, 3, 4, 3]
print(f"Next Greater: {s.nextGreater(arr)}")