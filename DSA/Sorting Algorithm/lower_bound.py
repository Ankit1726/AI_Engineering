def lower_bound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


arr = [2, 2, 2, 5, 7, 8]
x = 5

print(lower_bound(arr, x))