## Insertion Sort 
class Sorting:
    def insertion_sort(self,arr): #TC:O(n^2)
        n = len(arr)
        for i in range(1,n):
            curr = arr[i]
            prev = i-1
            while(prev>=0 and arr[prev]>curr):
                arr[prev+1] = arr[prev] # shift by its place 
                prev-=1
            arr[prev+1] = curr # place current element to its right position 
            prev-=1 

    def print_arr(self,arr):
        n = len(arr)
        for i in range(n):
            print(arr[i],end=" ")
        print()

res = Sorting()
arr = [4,1,5,2,3,9,7]
res.insertion_sort(arr)
res.print_arr(arr)