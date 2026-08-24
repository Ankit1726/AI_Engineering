## Search Single element in sorted array
class Sorting:
    def single_element(self, arr):
        n = len(arr)
        st, end = 0, n - 1

        # single element
        if n == 1:
            return arr[0]

        while st <= end:
            mid = st + (end - st) // 2

            if mid == 0 and arr[0] != arr[1]:
                return arr[mid]  # st
            if mid == n - 1 and arr[n - 1] != arr[n - 2]:
                return arr[mid]  # end

            # at mid
            if arr[mid - 1] != arr[mid] and arr[mid] != arr[mid + 1]:
                return mid

            # even size
            if mid % 2 == 0:
                if arr[mid - 1] == arr[mid]:  # left search
                    end = mid - 1
                else:
                    st = mid + 1
            else:  # odd size
                if arr[mid - 1] == arr[mid]:  # right search
                    st = mid + 1
                else:
                    end = mid - 1
        return -1


res = Sorting()
arr = [1, 1, 2, 2, 3, 4, 4, 5, 5]
ans = res.single_element(arr)
print(f"single element:{arr[ans]}")
