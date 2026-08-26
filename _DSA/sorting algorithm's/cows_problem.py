## Agressive Cow Problem
class Sorting:
    def isPossible(self, arr, n, c, minAllowDist): # TC:O(log(range)*m)
        cow, lastStalPos = 1, arr[0]
        for i in range(len(arr)):
            if arr[i] - lastStalPos >= minAllowDist:
                cow += 1
                lastStalPos = arr[i]
            if cow == c:
                return True
        return False

    def getDistance(self, arr, n, c):
        len(arr)
        arr.sort()
        st, end = 1, arr[n - 1] - arr[0]  # maxVal-minVal
        ans = -1
        while st <= end:
            mid = st + (end - st) // 2

            if self.isPossible(arr, n, c, mid):  # right search
                ans = mid
                st = mid + 1

            else:
                # left search
                end = mid - 1
        return ans

res = Sorting()
arr = [1,2,8,4,9]
answer = res.getDistance(arr,n=5,c=3)
print(f"largest minimum distance: {answer}")