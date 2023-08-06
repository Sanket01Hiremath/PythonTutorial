def is_palindrome(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            return "No"
    return "Yes"

print(is_palindrome("madams"))