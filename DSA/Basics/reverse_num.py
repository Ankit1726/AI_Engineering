## Reverse The Number 
def reverse_num(num):
    rev = 0  # TC:O(log n)
    while num>0:
        Ld = num%10
        rev = (rev*10) + Ld
        num = num//10
    return rev

print(reverse_num(1234))