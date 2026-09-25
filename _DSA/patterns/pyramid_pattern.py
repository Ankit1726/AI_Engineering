# --------------- Pyramid Pattern ---------------
class Pyramid_Pattern:
    def pyramid_pattern(self,n):
        for i in range(n):
            # spaces --> (n-i-1)
            for _ in range(n-i-1):
                print(" ",end=" ")

            # number --> 1 to i+1 
            for j in range(1,i+2):
                print(j,end=" ")

            # number --> i to 1 
            for j in range(i,0,-1):
                print(j,end=" ")
            print()

pyramid = Pyramid_Pattern()
pyramid.pyramid_pattern(n=4)