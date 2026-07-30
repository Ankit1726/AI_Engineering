def find_disappeared(arr):  #TC:O(n) & SC:O(n)
     n = len(arr)
     num_set = set(arr)           
     all_num = set(range(1, n + 1))
     miss_num = all_num - num_set
     return list(miss_num)        

arr = [1, 2, 3, 2, 1, 2, 3, 3, 7, 7, 8]
print(find_disappeared(arr))