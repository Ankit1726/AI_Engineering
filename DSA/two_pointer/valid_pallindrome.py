## Check palindrome String 
class Two_Pointer: 
    def vali_palindorme(self,str):
        left , right = 0 , len(str)-1
        while left < right:
            if(str[left]!=str[right]):
                return False
            left+=1
            right-=1
        return True

ans = Two_Pointer()
s = "madama"
print(ans.vali_palindorme(s))