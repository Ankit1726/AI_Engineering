## Remove Duplicaes From Sorted Array 
class Two_Pointer: 
    def remove_duplicates(self,num):
        if not num:return 0
        i = 0 
        for j in range(1,len(num)):
            if num[j]!=num[i]:
                i+=1
                num[i] = num[j]
        return num[:i+1]


ans = Two_Pointer()
num = [1, 1, 2, 2, 3, 4, 4]
print(ans.remove_duplicates(num))