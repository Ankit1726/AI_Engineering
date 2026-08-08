## Reverse String 
def reverse_str(str): # TC:O(n) & SC:O(n)
     words = str.split()
     words.reverse()
     res = " ".join(words)
     return res


## Get Largest Odd Number
class String:
     def largest_odd(self,str): # TC:O(n) & SC:O(1)
          n = len(str)
          for i in range(n-1,-1,-1):
               if int(str[i])%2 == 1:
                    return str[0:i+1]
          return " "

s = "54682724680"
sol = String()
ans = sol.largest_odd(s)
print(ans)