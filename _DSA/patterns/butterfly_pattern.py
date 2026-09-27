# -------------- Advanced Pattern ----------------
class Pattern:
    def butterfly(self, n):
        # Top Half
        for i in range(n):
            # Left stars: (i + 1) stars
            print("*" * (i + 1), end="")

            # Center spaces: 2 * (n - i - 1) spaces
            print(" " * (2 * (n - i - 1)), end="")

            # Right stars: (i + 1) stars
            print("*" * (i + 1), end="")

            # Move to next line
            print()

        # Bottom Half
        for i in range(n):
            # Left stars: (n - i) stars
            print("*" * (n - i), end="")

            # Center spaces: 2 * i spaces
            print(" " * (2 * i), end="")

            # Right stars: (n - i) stars
            print("*" * (n - i), end="")

            # Move to next line
            print()


p = Pattern()
p.butterfly(n=4)