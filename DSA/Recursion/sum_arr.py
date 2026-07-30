## Sum of Array 

def arr_sum(arr, n):
    # Base case: if the array size considered is 0, sum is 0
    if n == 0:
        return 0 
    return arr_sum(arr, n - 1) + arr[n - 1] 

arr = [1, 2, 3, 4, 5]
n = len(arr)
print(arr_sum(arr, n))  # Output: 15