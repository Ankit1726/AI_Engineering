## Painter Partiton Problem
class Sorting:

    def isPossible(self, arr, n, m, allowedTime): # C:O(log(range)*m)
        painter, time = 1, 0
        for i in range(len(arr)):
            if time + arr[i] <= allowedTime:
                time += arr[i]
            else:
                painter += 1
                time = arr[i]
        return painter <= m

    def painter_partition(self, arr, n, m):
        sum = 0
        n = len(arr)
        max_val = float("-inf")
        for i in range(n):
            sum += arr[i]
            max_val = max(max_val, arr[i])

        st, end = max_val, sum
        ans = -1
        while st <= end:
            mid = st + (end - st) // 2

            if self.isPossible(arr, n, m, mid):  # Left
                ans = mid
                end = mid - 1
            else:  # right
                st = mid + 1
        return ans


res = Sorting()
arr = [40, 30, 10, 20]
n, m = 4, 2
print(res.painter_partition(arr, n, m))
