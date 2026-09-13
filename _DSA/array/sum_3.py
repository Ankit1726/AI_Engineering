# 3 sum problem (2 pointer appraoch)

class array: # TC:O(n^2+n*logn) & SC:O(1)
    def sum_3(self, arr: list[int], tar: int) -> list[list[int]]:
        arr.sort()
        n = len(arr)
        ans = []

        if n < 3:
            return ans

        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                total_sum = arr[i] + arr[j] + arr[k]

                if total_sum > tar:
                    k -= 1
                elif total_sum < tar:
                    j += 1
                else:
                    # Found a valid triplet
                    ans.append([arr[i], arr[j], arr[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates ONLY after finding a valid triplet
                    while j < k and arr[j] == arr[j - 1]:
                        j += 1
                    while j < k and arr[k] == arr[k + 1]:
                        k -= 1
        return ans


obj = array()
arr = [-4, -1, -1, 0, 1, 2]
print(obj.sum_3(arr, tar=0))