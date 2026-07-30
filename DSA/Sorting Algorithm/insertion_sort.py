## Insertion Sort 
def insertion(arr):
    n = len(arr) # TC:O(n^2)

    for i in range(1,n):
        # current element as key 
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        
        # insert at correct position 
        arr[j+1] = key 
    return arr

arr = [13, 46, 24, 52, 20, 9]
print(insertion(arr))
