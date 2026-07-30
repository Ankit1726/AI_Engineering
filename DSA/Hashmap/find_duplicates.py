## Find Duplicates 
def find_duplicates(arr):
     hash_map = {}
     for i in arr:
          hash_map[i] = hash_map.get(i,0)+1

     for k,v in hash_map.items():
          if v>1:
               print(k)

arr = [1,2,2,3,4,4,5]
find_duplicates(arr)