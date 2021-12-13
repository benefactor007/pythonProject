def isPalPrint(s, indent='  '):
    print indent, 'isPalPrint called with', repr(s)
    if len(s) <= 1:
        print indent, 'About to return True from base case'
        return True
    else:
        ans = s[0] == s[-1] and isPalPrint(s[1:-1], indent + indent)
        print indent, 'About to return', ans, 'for', s
        return ans





def isPalindromnPrint(s):
    """Return Ture if a is a palindrome and False Otherwise"""
    return isPalPrint(toChars(s))


def toChars(s):
    import string
    s = string.lower(s)
    ans = ''
    # print s
    for c in s:
        if c in string.lowercase:
            ans = ans + c
        # print ans
    return ans

print isPalindromnPrint('abc')
print isPalPrint('121')