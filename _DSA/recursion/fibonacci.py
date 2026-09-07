## find fibonacci of nth number
class recursion:
    def fibonacci(self,n:int) -> int:
        if(n==0 or n==1):
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-1)

obj = recursion()
print(obj.fibonacci(5))