## Remove Occurnece of character in string 

class String:
    def remove_Occ(self,s:str,part:str) -> str:
        while part in s:
            s = s.replace(part,"",1)
        return s 

res = String()
str = "daabcbaabcbc"
part = "abc"
print(res.remove_Occ(str,part))