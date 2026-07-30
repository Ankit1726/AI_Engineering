## Print Divisor 
import math

def print_div(n):   # TC: O(√n)
    result = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            # Avoid duplicates
            if i != n // i:
                result.append(n // i)
    return sorted(result)
print(print_div(12))