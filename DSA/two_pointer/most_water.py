## Container With Most Water  
class Two_Pointer:
    def most_water(self,ht):
        left,right = 0,len(ht)-1
        max_area = 0
        while(left<right):
            width = right-left
            area  = width * min(ht[left],ht[right])
            max_area = max(max_area,area)

            if(ht[left]<ht[right]):
                left+=1
            else:
                right-=1
        return max_area


ans = Two_Pointer()
ht = [1,8,6,2,5,4,8,3,7]
print(ans.most_water(ht))