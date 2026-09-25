# -------------- Advanced Pattern ----------------
class Pattern:
    def inverted_trianlge(self,n):
        for i in range(n):
            # print i spaces 
            for _ in range(i):
                print(" ",end=" ")

            # print (n-i) number 
            for _ in range(n-i):
                print(i+1,end=" ")
            print()

    def inverted_character(self, n):
        for i in range(n):
            # Print i leading spaces
            for _ in range(i):
                print(" ", end=" ")

            # Convert row index to character ('A', 'B', 'C', ...)
            ch = chr(ord("A") + i)

            # Print (n - i) characters
            for _ in range(n - i):
                print(ch, end=" ")

            # Move to the next line
            print()

p = Pattern()
p.inverted_trianlge(n=5)
p.inverted_character(n=5)