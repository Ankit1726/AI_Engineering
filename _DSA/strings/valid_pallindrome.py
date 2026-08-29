## Check Valid Palindrome 

class String:
    def isAlphaNum(self,ch:str) -> bool:
        return ch.isalnum() # (0-9, a-z, A-Z)

    def isPallindrome(self,s:str) -> bool:
        st,end = 0,len(s)-1
        while st<end:
            # skip non alpha numeric characters from start & end
            if not self.isAlphaNum(s[st]):
                st+=1 
                continue

            if not self.isAlphaNum(s[end]):
                end-=1
                continue

            if s[st].lower()!=s[end].lower():
                return False

            st+=1 
            end-=1
        return True

res = String()
s = "ma4da4dam"
print(res.isPallindrome(s))