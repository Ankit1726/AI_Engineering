## Print N to 1 Seires 
def printfunc(n):
    if n==0:
        return
    print(n,end=" ")
    printfunc(n-1)

printfunc(10)