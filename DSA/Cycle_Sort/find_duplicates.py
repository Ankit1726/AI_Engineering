## Find Duplicates In an Array 

def find_suplicates(arr): # TC:O(n)
     sorted_arr = sorted(arr)
     n = len(sorted_arr)
     for i in range(1,n):
          if(sorted_arr[i-1]== sorted_arr[i]):
               return sorted_arr[i]
     return -1 


## Find Duplicates In an Array  Using Cycle Sort
def Duplicates_cycleSort(arr):
    i = 0
    n = len(arr)  # TC:O(n) SC:O(n)

    while i < n:
        correct = arr[i] - 1

        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1

    ans = []

    for i in range(len(arr)):
        if arr[i] != i + 1:
            ans.append(arr[i])

    return ans

arr = [1,2,3,3,4]
# print(find_suplicates(arr))
print(Duplicates_cycleSort(arr))
