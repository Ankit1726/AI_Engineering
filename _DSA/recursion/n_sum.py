## caculate sum of n number 
class recursion:
    def n_sum(self,n:int) -> int: # SC:O(call stack space(n))
        if(n==1):
            return 1
        return n+self.n_sum(n-1)

    def itr_sum(self,n:int)-> int: # SC:O(1)
        sum = 0
        for i in range(n):
            sum+=i
        print(f"sum of {5} numbers :{sum}")

obj = recursion()
print(obj.n_sum(n=7))
obj.itr_sum(n=5)