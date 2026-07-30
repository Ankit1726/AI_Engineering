## First Non Repeating 

def unique_char(str):
     freq = {}
     for i in str:
          freq[i] = freq.get(i,0)+1

     for ch in str:
          if freq[ch] == 1:
               return ch 
   

str = "abbcdeef"
print(unique_char(str))