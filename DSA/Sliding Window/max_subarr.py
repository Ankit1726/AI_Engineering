class Solution:
    def max_subarr(self, arr, k):
        n = len(arr)

        if k > n:
            return -1

        # First window
        window_sum = 0
        for i in range(k):
            window_sum += arr[i]
        ans = window_sum

        # Remaining windows
        for i in range(k, n):
            window_sum -= arr[i - k]
            window_sum += arr[i]
            ans = max(ans, window_sum)

        return ans


arr = [1, 2, 5, 4, 9, 4]
k = 3

sol = Solution()
print(sol.max_subarr(arr, k))