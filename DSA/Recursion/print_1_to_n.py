## Print ! to N
def printfunc(n):
    if n==0:
        return
    printfunc(n-1)
    print(n,end=" ")

printfunc(5)