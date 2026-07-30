class Solution:
    def rearrange(self, arr):
        n = len(arr)
        res = [0] * n
        pos_idx = 0
        neg_idx = 1

        for i in range(n):
            if arr[i] >= 0:
                res[pos_idx] = arr[i]
                pos_idx += 2
            else:
                res[neg_idx] = arr[i]
                neg_idx += 2

        return res


arr = [3, 1, -2, -5, 2, -4]
sol = Solution()
print(sol.rearrange(arr))