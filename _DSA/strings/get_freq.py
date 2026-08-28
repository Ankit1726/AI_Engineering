## Get frequency of character 
class String:
    def freq_count(self,s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        print(freq)

res = String()
s = "hello"
res.freq_count(s)
print("-"*30)
# using inbuilt counter funciton 
from collections import Counter

freq = Counter(s)
print(freq)