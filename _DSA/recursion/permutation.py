## find all permutations of given number
class recursion:

    def get_permutation(self, arr: list[int], idx: int, ans: list[int]):
        if idx == len(arr):
            # Append a copy of the current state of arr
            ans.append(arr.copy())
            return

        for i in range(idx, len(arr)):
            # Swap
            arr[idx], arr[i] = arr[i], arr[idx]

            # Recurse for next index
            self.get_permutation(arr, idx + 1, ans)

            # Backtrack step
            arr[idx], arr[i] = arr[i], arr[idx]

    def permutation(self, arr: list[int]) -> list[int]:
        ans = []
        self.get_permutation(arr, 0, ans)
        return ans


obj = recursion()
arr = [1, 2, 3]
result = obj.permutation(arr)
print(result)
