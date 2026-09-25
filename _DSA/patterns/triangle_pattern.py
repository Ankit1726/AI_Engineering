# --------------- Traingle Pattern ----------------
class Triangle:
    def star_triangle(self,n):
        for i in range(n):
            for _ in range(i+1):
                print("*",end=" ")
            print()
        print()

    def num_triangle(self,n):
        for i in range(1,n+1):
            for _ in range(i):
                print(i,end=" ")
            print()
        print()

    def print_triangle(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()
        print()

    def reverse_triangle(self,n):
        for i in range(1,n+1):
            for j in range(i,0,-1):
                print(j,end=" ")
            print()
        print()

    def floyd_triangle(self,n):
        num = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(num,end=" ")
                num+=1
            print()
        print()

t = Triangle()
t.star_triangle(n=5)
t.num_triangle(n=5)
t.print_triangle(n=4)
t.reverse_triangle(n=5)
t.floyd_triangle(n=4)