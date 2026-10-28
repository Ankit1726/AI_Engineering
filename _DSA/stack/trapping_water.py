## -------------- Trapping Rain Water ------------------
class Two_Pointer: # TC:O(n) & SC:O(1)
    def trap_water(self, hieght: list[int]) -> int:
        n = len(hieght)
        ans = 0
        left, right = 0, n - 1
        left_max, right_max = 0, 0

        if n < 3:
            return 0

        while left < right:
            left_max = max(left_max, hieght[left])
            right_max = max(right_max, hieght[right])

            if left_max < right_max:  # left case
                ans += left_max - hieght[left]
                left += 1
            else:  # right case
                ans += right_max - hieght[right]
                right -= 1
        return ans


res = Two_Pointer()
hieght = [4, 2, 0, 3, 2, 5]
print(f"Total Water Trapped: {res.trap_water(hieght)}")