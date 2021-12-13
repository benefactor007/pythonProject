import math


def printLogarithm(x):
    if x <= 0:
        print " Positive numbers only, please"
        return  # One reason to use it is if you detect an error condition.

    result = math.log(x)
    print "The log of x is", result


def countdown(n):
    if n == 0:
        print "Blastoff"

    else:
        print n
        countdown(n - 1)


def nLines(n):
    if n > 0:
        print
        nLines(n - 1)


def compare(x, y):
    if x < y:
        print x, "is less than", y
    elif x > y:
        print x, "is greater than", y
    else:
        print x, "and", y, "are equal"


def dispatch(choice):
    if choice == 'A':
        functionA()
    elif choice == 'B':
        functionB()
    elif choice == 'C':
        functionC()
    else:
        print "Invalid choice"


"""Minimal program of infinite recursion"""


def recurse():
    recurse()


name = raw_input("What...is your name? ")
print name

prompt = "What... is the airspeed velocity of an unladen swallow?\n"
# Use the input function, when we expect the response to be an integer.
speed = input(prompt)
print 'The airspeed velocity is', speed

message = "What's up, Doc"
# if the string contains a single quote (or an apostrophe, which is the same character), you have to use double
# quotes to enclose it.

"""Python has twenty-nine keywords: 
and       def       exec      if        not       return 
assert    del       finally   import    or        try 
break     elif      for       in        pass      while 
class     else      from      is        print     yield 
continue  except    global    lambda    raise """
