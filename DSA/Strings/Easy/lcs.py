class Solution:
    def LCS(self, str_list):   # TC: O(n*m), SC: O(1)
        if len(str_list) == 0:
            return ""

        base_str = str_list[0]
        res = ""

        for i in range(len(base_str)):
            for word in str_list[1:]:
                if i == len(word) or word[i] != base_str[i]:
                    return res
            res += base_str[i]

        return res


str_list = ["FLOWER", "FLOW", "FLOWN"]

sol = Solution()
ans = sol.LCS(str_list)
print(ans)