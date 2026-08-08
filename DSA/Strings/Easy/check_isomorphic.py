class Solution:
    def check_iso(self, s, t):  # TC:O(n) & SC:O(n)
        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # s -> t mapping
            if char_s in map_s:
                if map_s[char_s] != char_t:
                    return False
            else:
                map_s[char_s] = char_t

            # t -> s mapping
            if char_t in map_t:
                if map_t[char_t] != char_s:
                    return False
            else:
                map_t[char_t] = char_s

        return True


s = "BADC"
t = "BABA"

sol = Solution()
print(sol.check_iso(s, t))