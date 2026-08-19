## Trapping Rain Water Problem 
class Two_Pointewr:
    def trap_rainWater(self,ht):
        left,right = 0,len(ht)-1
        ans = 0
        l_max , r_max = 0,0 
        while(left<right):
            l_max = max(l_max,ht[left])
            r_max = max(r_max,ht[right])

            if(l_max<r_max):
                # for left 
                ans+=(l_max - ht[left])
                left+=1
            else:
                ans+=(r_max-ht[right])
                right-=1
        return ans 

res = Two_Pointewr()
height = [4,2,0,3,2,5]
print(res.trap_rainWater(height))