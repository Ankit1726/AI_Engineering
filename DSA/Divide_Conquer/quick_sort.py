def quick_sort(arr, low, high): # TC:O(nlog n) SC:O(1)
    if(len(arr)<=1):
        return arr
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high] # last element
    i = low - 1  # tracks elements smaller than pivot
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap if element is less than or equal to pivot
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
     
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)