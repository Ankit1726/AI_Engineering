## calculate factorial of n number 
class recursion:
    def factorial(self,n:int) -> int:
        if(n==0):
            return 1
        return n*self.factorial(n-1)

    def itr_fact(self,n:int) -> int:
        fact = 1
        for i in range(1,n+1):
            fact = fact*i
        print(f"factorial of {n}:{fact}")


obj = recursion()
print(obj.factorial(n=5))
obj.itr_fact(n=5)