## Merge 2 Subarrays 
class Two_Pointer:
    def merge(self,ar1,ar2):
        i,j = 0,0 
        res =  []
        while(i<len(ar1) and j<len(ar2)):
            if(ar1[i]<ar2[j]):
                res.append(ar1[i])
                i+=1
            else:
                res.append(ar2[j])
                j+=1
        res.extend(ar1[i:])
        res.extend(ar2[j:])
        return res

ans = Two_Pointer()
ar1,ar2 = [1,3,5,7],[2,4,6,8]
print(ans.merge(ar1,ar2))