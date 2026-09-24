# --------------- Square Pattern -----------------

class Square_Patterns:
    def num_pattern(self,n):
        for i in range(1,n):
            for j in range(1,n):
                print(j,end=" ")
            print()
        print()

    def dynamic_num(self,n):
        num = 1
        for _ in range(n):
            for _ in range(n):
                print(num,end=" ")
                num+=1 
            print()
        print()

    def star_pattern(self,n):
        for _ in range(n):
            for _ in range(n):
                print("*",end=" ")
            print()
        print()

    def static_alhpabet(self,n):
            for _ in range(n):
                ch = 'A'
                for _ in range(n):
                    print(ch,end=" ")
                    ch = chr(ord(ch) + 1)
                print()
            print()

    def dynamic_alphabet(self,n):
        ch = 'A'
        for _ in range(n):
            for _ in range(n):
                print(ch,end=" ")
                ch = chr(ord(ch) + 1)
            print()
        print()

sq = Square_Patterns()
sq.num_pattern(n=5)
sq.star_pattern(n=5)
sq.dynamic_alphabet(n=4)
sq.static_alhpabet(n=4)
sq.dynamic_num(n=3)