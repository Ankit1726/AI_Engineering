## Selection Sort 
class Sorting:
    def selection_sort(self,arr): #TC:O(n^2)
        n = len(arr)
        for i in range(0,n-1):
            small_idx = i # unsorted start 
            for j in range(i+1,n):
                if(arr[j]<arr[small_idx]):
                    small_idx = j 
            # swap 
            arr[i],arr[small_idx] = arr[small_idx],arr[i]

    def print_arr(self,arr):
        n = len(arr)
        for i in range(n):
            print(arr[i],end=" ")
        print()

res = Sorting()
arr = [4,1,5,2,3,7,11,9]
res.selection_sort(arr)
res.print_arr(arr)