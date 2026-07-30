## Check Prime Number 
from math import sqrt
def isPrime(n):
    if n==1: # TC: O(√n)
        return False
    
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True

print(isPrime(20))