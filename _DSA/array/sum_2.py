## 2Sum Problem Using Hashing Concept 
class array:
    def sum_2(self,arr,target): # TC:O(n)
        map = {} # dictionary 
        n = len(arr)
        for i in range(n):
            first = arr[i]
            second = target - first

            if second in map:
                return [i,map[second]]
            map[first] = i 
        return []

obj = array()
arr = [5,2,11,7,15]
print(obj.sum_2(arr,target=9)) # indices