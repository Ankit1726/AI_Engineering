## Print Sum of Divisor
import math

def divisor_sum(n):
    sum = 0 # TC:O(√n)
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):
            sum+=i
            # Add Paired Sum
        if(i!=n//i):
            sum+=n//i
    return sum
        
print(divisor_sum(12))