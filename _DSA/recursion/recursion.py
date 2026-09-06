## Recursion Concept & Problems 
class recursion:
    # print n to 1
    def printDec(self,n:int) -> int:
        # base calls 
        if(n==0):
            return 
        print(n,end=" ")
        self.printDec(n-1)

    def printInc(self,n:int)-> int:
        # base case
        if(n==0):
            return
        self.printInc(n-1)
        print(n,end=" ")


obj = recursion()
obj.printDec(n=5)
print()
obj.printInc(n=5)