## -------------- Stock Span Problem --------------- 
class Stack:
    def stock_span(self,prices): # O(n) & O(n)
        n = len(prices)
        stack = []
        span = [0]*n

        for i in range(n):
            while stack and prices[stack[-1]] <= prices[i]:
                stack.pop()

            if not stack:
                span[i] = i+1 
            else:
                span[i] = i-stack[-1]

            # push current index to stack 
            stack.append(i)
        return span

s = Stack()
prices = [100, 80, 60, 70, 60, 75, 85]
print(s.stock_span(prices))