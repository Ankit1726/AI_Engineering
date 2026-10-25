## --------------- Next Greater Element --------------- 
class Stack:
    def next_greater(self,arr): # TC:O(n) & SC:O(n)
        n = len(arr)
        ans = [-1] * n 
        stack = []

        # Traverse Backward 
        for i in range(n-1,-1,-1):
            # element <= curr --> pop from stack 
            while stack and stack[-1]<=arr[i]:
                stack.pop()

            # stack top --> next greater element 
            if stack:
                ans[i] = stack[-1]

            stack.append(arr[i])
        return ans 

s = Stack()
arr = [6, 8, 0, 1, 3]
print(s.next_greater(arr))