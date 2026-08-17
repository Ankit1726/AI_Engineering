## Move Zeroes To End
class Two_Pointer: 
    def move_zeroes(self,num):
        if not num:return 0 
        i = 0
        for j in range(0,len(num)):
            if(num[j]!=0):
                # Swap 
                num[i],num[j] = num[j],num[i]
                i+=1
        return num

ans = Two_Pointer()
num = [0, 1, 0, 3, 12]
print(ans.move_zeroes(num))