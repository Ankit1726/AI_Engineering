## Bubble Sort 
def bubble(arr):
    n = len(arr)

    for i in range(n-1): # TC:O(n) Best Case 
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                #swap -> True
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        
        if not swapped:
            break
    return arr

arr = [1,2,7,4,8,9]
print(bubble(arr))