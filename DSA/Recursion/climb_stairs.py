# Clibing Stairs 
def climb_stairs(n):
     if(n==0):
          return 1 # 1 step 
     elif(n<=0):
          return 0 
     else:
          return climb_stairs(n-1)+climb_stairs(n-2)
     
print(f"Possible Ways:{climb_stairs(5)}")