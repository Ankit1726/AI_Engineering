## Check Number is Pallindrome 

def Pallindrome(n):
    if n<0:  # TC:O(log n)
        return False
    num = n
    rev=0
    while num>0:
        Ld = num%10
        rev = (rev*10)+Ld
        num//=10
    return rev == n

print(Pallindrome(1221))