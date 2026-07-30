def palindrome(s, st, end):
    # Base case
    if st >= end:
        return True

    # Character mismatch
    if s[st] != s[end]:
        return False

    # Recursive call
    return palindrome(s, st + 1, end - 1)
s = "madam"
print(palindrome(s, 0, len(s) - 1))