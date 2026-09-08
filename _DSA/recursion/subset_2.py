## Get all subset (duplicates not allowed)
class recursion:

    def get_subset(self, arr, ans, i, allsubsets):
        if i == len(arr):
            # Append a copy of 'ans', not the reference
            allsubsets.append(ans.copy())
            return

        # Include choice
        ans.append(arr[i])
        self.get_subset(arr, ans, i + 1, allsubsets)

        # Backtrack step
        ans.pop()

        # Exclude choice (skip all duplicates of the current element)
        idx = i + 1
        while idx < len(arr) and arr[idx] == arr[i]:
            idx += 1
        self.get_subset(arr, ans, idx, allsubsets)


obj = recursion()
arr = [1, 2, 2]

# Ensure the array is sorted before processing
arr.sort()

ans = []
allsubsets = []
obj.get_subset(arr, ans, 0, allsubsets)
print(allsubsets)
