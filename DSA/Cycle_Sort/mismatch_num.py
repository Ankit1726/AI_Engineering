## Set Mismatch  # Tc:O(n) SC:O(1)
def find_mismatch(arr):
     sorted_arr = sorted(arr)
     dup = -1
     n = len(sorted_arr)
     exp_sum = (n*(n+1))//2

     # find duplicates 
     for i in range(1,n):
          if(sorted_arr[i] == sorted_arr[i-1]):
               dup = sorted_arr[i]
               break
     actual_sum = sum(sorted_arr) - dup
     missing_num = exp_sum - actual_sum
     return[dup,missing_num]

## Set Mismatch Using Cycle Sort
def find_misdup(nums): 
    i = 0

    while i < len(nums):
        correct = nums[i] - 1

        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]
        
arr = [1,2,2,4]
print(find_mismatch(arr))
print(find_misdup(arr))