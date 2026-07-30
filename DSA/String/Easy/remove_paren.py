## Remove Outermost Parenthesis

class String:
     def remove_outermost(self,str): #TC:O(n) & SC:O(1)
          res = ""
          count = 0
          for ch in str:
               if(ch=="("):
                    count+=1
                    if(count>1):
                         res+=ch
               else:
                    count-=1
                    if(count>0):
                         res+=ch
          return res

str = "(()())(())"
sol = String()
ans = sol.remove_outermost(str)
print(ans)