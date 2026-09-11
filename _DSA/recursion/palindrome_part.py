## Palindrome Partioning Problem 
class backtrack:
    def is_palindrome(self,s:str) -> bool: # TC:O(n*2^n)
        return s == s[::-1]

    def helper(self,s:str,partitions:list[str],ans:list[list[str]]):
        if len(s)==0:
            ans.append(list(partitions))
            return

        for i in range(len(s)):
            str_part = s[:i+1]

            if self.is_palindrome(str_part):
               
                partitions.append(str_part) # chhose cut
                self.helper(s[i+1:],partitions,ans) # recursive call
                # backtrack 
                partitions.pop()

    def getPartition(self,s:str) -> list[list[str]]:
        ans = []
        partitions = []
        self.helper(s,partitions,ans)
        return ans 

obj = backtrack()
s="aab"
print(obj.getPartition(s))
