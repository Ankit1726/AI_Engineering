## ---------------- Prevoius Smaller ---------------------- 
class Stack:
    def prevoius_small(self,arr): # TC:O(n) & SC:O(n)
        n = len(arr)
        ans = [-1] * n 
        stack  = []

        for i in range(n):
            # pop element --> stack[top] >= arr[i]
            while stack and stack[-1]>=arr[i]:
                stack.pop()

            # empty stack --> add -1 in ans 
            if not stack:
                ans[i] = -1 
            else:
                ans[i] = stack[-1]

            # push current element on the stack 
            stack.append(arr[i])
        return ans 

s = Stack()
arr = [3, 1, 0, 8, 6]
print(f"Previous Smaller Elements: {s.prevoius_small(arr)}")