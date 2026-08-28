## Reverse Given String 

class String:
    def reverse(self, str_val: str) -> str:
        # Convert string to list since strings are immutable
        s_list = list(str_val)
        st, end = 0, len(s_list) - 1

        while st < end:
            s_list[st], s_list[end] = s_list[end], s_list[st]
            st += 1
            end -= 1
        return "".join(s_list)

res = String()
s = "banana"
print(res.reverse(s))  # Output: ananab