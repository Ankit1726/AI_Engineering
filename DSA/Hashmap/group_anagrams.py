## Group Anagram 
from collections import defaultdict

def group_anagram(words):
     groups = defaultdict(list)

     for w in words:
          key = "".join(sorted(w))
          groups[key].append(w)
     return list(groups.values())

words=["eat","tea","ate","bat"]
print(list(group_anagram(words)))