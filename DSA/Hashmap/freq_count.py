## Count Frequency 

def count_freq(arr):
     freq = {}
     for i in arr:
          if i in freq:
               freq[i] +=1
          else:
               freq[i] = 1
     return freq

arr = [1,2,2,3,3,3]
print(count_freq(arr))