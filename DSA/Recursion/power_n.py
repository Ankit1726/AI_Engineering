## Power od x^n
def power(x,n):
    if n==0:
        return 1
    half = power(x,n//2)
    if n%2==0:
        return half * half # even case 
    return x*half*half # odd case 

print(power(2,5))