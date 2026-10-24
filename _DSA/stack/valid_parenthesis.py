## Valid Parenthesis
class Stack:
    def isValid(self, s: str) -> bool:  # O(n)
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"

                # check poped element is matched or not
                if mapping[char] != top_element:
                    return False
            else:  # new bracket added
                stack.append(char)
        return not stack


s = Stack()
str = "([{}])"
print(s.isValid(str))