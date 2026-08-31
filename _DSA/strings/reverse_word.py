## Reverse words in string 
class String:
    def reverseWords(self,s:str)-> str:
        # reverse entire string 
        s_list = list(s)
        s_list.reverse()

        n = len(s_list)
        ans = ""
        i = 0 

        while  i<n:
            word_chars = []
            # extract single word 
            while i<n and s_list[i]!=" ":
                word_chars.append(s_list[i])
                i+=1 

            # reverse back into original form 
            word_chars.reverse()
            word = "".join(word_chars)

            if(len(word))>0:
                ans+=" "+word
            i+=1
        return ans[1:] # remove extra space 

res = String()
s = "the pen"
answer = res.reverseWords(s)
print(answer)
