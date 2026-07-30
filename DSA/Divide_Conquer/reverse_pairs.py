class Solution:

    def reversePair(self, nums):
        self.count = 0

        def divide(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = divide(arr[:mid])
            right = divide(arr[mid:])

            # Count reverse pairs
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] > 2 * right[j]:
                    self.count += len(left) - i
                    j += 1
                else:
                    i += 1

            # Merge Step
            merged = []
            l = 0
            r = 0

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1

            merged.extend(left[l:])
            merged.extend(right[r:])
            return merged

        divide(nums)
        return self.count


arr = [1, 3, 2, 3, 1]
obj = Solution()
print(obj.reversePair(arr))