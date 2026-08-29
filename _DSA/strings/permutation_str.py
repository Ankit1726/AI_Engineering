## Find permutations in given string 
class String:
    def isFreqSame(self, freq1: list, freq2: list) -> bool:
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True

    def checkPermutation(self, s1: str, s2: str) -> bool:
        # Step 1: Count frequencies of characters in s1
        freq = [0] * 26
        for ch in s1:
            freq[ord(ch) - ord('a')] += 1
        windSize = len(s1)

        # Step 2: Iterate over s2 using a window of size len(s1)
        for i in range(len(s2)):
            windIdx = 0
            idx = i
            windFreq = [0] * 26

            # Build frequency array for current window
            while windIdx < windSize and idx < len(s2):
                windFreq[ord(s2[idx]) - ord('a')] += 1
                windIdx += 1
                idx += 1

            # Check if current window matches s1's frequencies
            if self.isFreqSame(freq, windFreq):
                return True
        return False

res = String()
s1 = 'ab'
s2 = 'eidbaooo'
ans = res.checkPermutation(s1,s2)
print(f"s1 = '{s1}', s2 = '{s2}' -> Result: {ans}")