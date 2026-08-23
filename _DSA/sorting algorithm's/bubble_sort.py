## Bubble Sort 
class Sorting: 
    def bubble_sort(self,arr): # TC:O(n^2)
        n = len(arr)
        for i in range(0,n-1):
            isSwap = False
            for j in range(0,n-i-1):
                if(arr[j]>arr[j+1]):
                    # swap 
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    isSwap = True
            if(not isSwap):
                return

    def print_arr(self,arr):
        n = len(arr)
        for i in range(n):
            print(arr[i],end=" ")
        print()

res = Sorting()
arr = [3,1,2,7,5,4,8]
res.bubble_sort(arr)
res.print_arr(arr)