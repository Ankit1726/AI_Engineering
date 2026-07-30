# Count Digit 
def count_digit(num:int) -> int:
    count = 0 # TC:O(log n)
    n = num
    while n >0:
        count+=1
        n = n//10
    return count

print(count_digit(34534))