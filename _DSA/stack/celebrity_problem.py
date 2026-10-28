## --------------- Celebrity Problem ------------------
class Stack:  # TC:O(n) & SC:O(n)
    def celebrity_problem(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        if n == 0:
            return -1

        stack = list(range(n))

        # find candidate using elimination method
        while len(stack) > 1:
            i = stack.pop()
            j = stack.pop()

            # i knows j then i can not be celebrity (pushback j)
            if matrix[i][j] == 1:
                stack.append(j)
            else:  # otherwise j can not become celebrity (pushback i)
                stack.append(i)

        if not stack:
            return -1
        celebrity = stack.pop()

        # verify celebrity potential
        for i in range(n):
            if (i != celebrity) and (
                matrix[i][celebrity] == 0 or matrix[celebrity][i] == 1
            ):
                return -1
        return celebrity


s = Stack()

matrix = [[0, 1, 0], [0, 0, 0], [0, 1, 0]]
print(f"Celebrity index: {s.celebrity_problem(matrix)}")