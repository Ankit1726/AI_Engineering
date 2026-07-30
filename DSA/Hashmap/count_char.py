## Count Characters 

def count_char(str):
     hash_map = {}
     for char in str:
          hash_map[char] = hash_map.get(char,0)+1
     return hash_map

str = "banana"
print(count_char(str))