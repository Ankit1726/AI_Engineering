from typing import List

class Solution:
    def rotate(self, arr: List[int], k: int):

        n = len(arr)
        k %= n

        def reverse(left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        # Step 1
        reverse(n-k, n-1)

        # Step 2
        reverse(0, n-k-1)

        # Step 3
        reverse(0, n-1)


arr = [1,2,3,4,5,6]
k = 3

sol = Solution()
sol.rotate(arr, k)

print(arr)