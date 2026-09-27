# -------------- Advanced Pattern ----------------
class Pattern:
    def hollow_diamond(self, n):
        # Top Half
        for i in range(n):
            # Outer spaces: (n - i - 1) spaces
            print(" " * (n - i - 1), end="")

            # First star
            print("*", end="")

            # Inner spaces and second star (if not the first row)
            if i != 0:
                print(" " * (2 * i - 1), end="")
                print("*", end="")
            
            # Move to the next line (MUST BE INSIDE TOP LOOP)
            print()

        # Bottom Half
        for i in range(n - 1):
            # Outer spaces: (i + 1) spaces
            print(" " * (i + 1), end="")

            # First star
            print("*", end="")

            # Inner spaces and second star (if not the last row)
            if i != n - 2:
                print(" " * (2 * (n - i) - 5), end="")
                print("*", end="")
            
            # Move to the next line
            print()

p = Pattern()
p.hollow_diamond(n=5)