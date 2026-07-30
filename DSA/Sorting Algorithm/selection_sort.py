## Selection Sort 
def selection(arr):
    n = len(arr)  # TC:O(n^2)

    # find minimum element 
    for i in range(n):
        min_idx = i
        # compare with another element
        for j in range(i+1,n):
            if (arr[j]<arr[min_idx]):
                min_idx = j
        
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
print(selection(arr))