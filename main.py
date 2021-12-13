# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def Hanoi(n,f,t,s):
    if n==1:
        print 'move' + n +' from ' + f + ' to ' + t
    else:
        Hanoi(n-1,f,s,t)
        Hanoi(1,f,t,s)
        Hanoi(n-1,s,t,f)

def toChars(s):
    import string
    s = string.lower(s)
    ans = ''
    #print s
    for c in s:
        if c in string.lowercase:
            ans = ans + c
           # print ans
    return ans

print toChars('ABC asdajd dasdjoaisjd')
Hanoi(1,'f','t','s')
#Hanoi(5,'f','t','s')

