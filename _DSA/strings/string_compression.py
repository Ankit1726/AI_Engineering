## String Compression Problem 
class String:
    def compress_str(self,chars:list[str]):
        idx,i=0,0 
        n = len(chars)

        while i<n:
            ch = chars[i]
            count = 0

            # count occurence 
            while i<n and chars[i] == ch:
                count+=1
                i+=1

            # always write character 
            chars[idx] = ch 
            idx+=1 

            # if count > 1 (convert count digit to string and add)
            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx+=1 
        return chars 

res = String()
chars = ["a","a","b","b","c","c","c"]
answer = res.compress_str(chars)
print(answer)
