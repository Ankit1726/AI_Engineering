## 3 Sum Problem
class Two_Pointer:
    def sum_3(self, arr):
        n = len(arr)
        arr.sort()
        res = []

        for i in range(n - 2):
            # Skip duplicate first element
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                if total == 0:
                    res.append([arr[i], arr[left], arr[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1

                    # Skip duplicate right
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res


ans = Two_Pointer()
arr = [-1, 0, 1, 2, -1, -4]
print(ans.sum_3(arr))