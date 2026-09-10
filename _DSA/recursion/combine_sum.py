# Tar in maze problem

class Backtracking: # TC:O(2^n)
    def helper(self,arr: list[int],idx: int,target: int,combin: list[int],ans: list[list[int]],seen_set: set,
    ):
        # Target achieve ho gaya
        if target == 0:
            combin_tuple = tuple(combin)
            # Duplicate check using set
            if combin_tuple not in seen_set:
                seen_set.add(combin_tuple)
                ans.append(list(combin))
            return

        if idx == len(arr) or target < 0:
            return

        # Single Include 
        combin.append(arr[idx])
        self.helper(arr, idx + 1, target - arr[idx], combin, ans, seen_set)

        # Multiple Include 
        self.helper(arr, idx, target - arr[idx], combin, ans, seen_set)

        # Backtrack Step
        combin.pop()

        # Exclude Choice 
        self.helper(arr, idx + 1, target, combin, ans, seen_set)

    def combinationSum(self, arr: list[int], target: int) -> list[list[int]]:
        ans = []
        seen_set = set()  
        self.helper(arr, 0, target, [], ans, seen_set)
        return ans


obj = Backtracking()
arr = [2, 3, 5]
target = 8
print(obj.combinationSum(arr, target))
