# coding=utf-8
def easySort(L):
    for i in range(len(L) - 1):
        """Traversal of L"""
        mindex = i
        print "mindex is ", mindex
        minVar = L[i]
        print "minVar is ", minVar
        j = i + 1
        while j < len(L):
            if minVar > L[j]:
                mindex = j
                minVar = L[j]
            j += 1
        temp = L[i]
        L[i] = L[mindex]
        L[mindex] = temp
        print "The partially sort list is ", L

    return 0


L = [1, 4, 5, 23, 21321, 3214123432, 2, 1, 321312312, 1, 221]

# print easySort(L)

fruit = "Banana"
word1 = "Encapsulation"


def TraversalStr(str):
    index = 0
    while index < len(fruit):
        letter = fruit[index]
        print letter
        index += 1


# Traversal backward
"""As an exercise, write a function that takes a string as an argument and outputs the letters backward, one per line."""


def Tbackward(str):  # string as an argument.
    for i in range(len(str)):
        # print "i is", i
        i += 1
        letter = str[-i]
        print letter, '\t',
    print
    return


Tbackward(fruit)
Tbackward(word1)

"""Make way for duckling"""


def Ducking():
    prefixes = "ABCDEFGHIJKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        if letter == "O" or letter == "Q":
            print letter + "u" + suffix, '\t',
        else:
            print letter + suffix, '\t',
    print


def comparsionFruit(word):
    Fword = word.lower()
    if Fword > fruit:
        print "Your word, " + word + ", comes before ", fruit
    elif Fword < fruit:
        print "Your word, " + word + ", comes after ", fruit
    else:
        print "Yes, we have no ", fruit, "s!"
    print


def demoStringImmutable():
    greeting = "Hello world!"
    try:
        greeting[1] = "J"  # Error
    except Exception:  # Remove error
        print "Cuz string is immutable", '\n',

    NewGreeting = "J" + greeting[1:]
    print NewGreeting
    print


def find(str, char, pos=0):
    # print "The length of string is ", len(str)
    index = 0
    findlist = []
    for pos in range(len(str)):
        if str[pos] == char:
            # print "find the char, ", str[pos], ", in the index of ", pos
            findlist.append(pos)
            print "The findlist shows ", findlist
            # index += 1
            # print "pos is", pos
        elif pos == len(str) - 1 and findlist == []:
            print False
            return False
    return


find("scavenge", "d", 0)
Ducking()
print fruit[:]
comparsionFruit("Apple")
comparsionFruit("apple")
comparsionFruit("orange")
comparsionFruit("Orange")

demoStringImmutable()
find("scavenged", "d")
print find("scavenge", "d", 0)


def countletters(str, letter):
    count = 0
    for char in str:
        if char == letter:
            count += 1
    print count
    return


countletters("Banana", "a")

import string


def demoStringFind():
    fruit = "banana"
    index = string.find(fruit, "a")
    print index
    print string.find(fruit, "na")
    print string.find(fruit, "na", 3)
    print string.find("bob", "b", 1, 2)


demoStringFind()


def isLower(ch):
    return string.find(string.lowercase, ch) != -1


# Alternative way

def isLower1(ch):
    return ch in string.lowercase


"""the string， string.lowercase, contains all of the letters that the system considers to be lowercase."""


def isLower2(ch):
    return "a" <= ch <= "z"

# cursor ˈkərsər 光标

print isLower("Fruit"),"\t", isLower1("Fruit"),"\t", isLower2("Fruit")
print string.whitespace
"""The constant string.whitespace contains all the whitespace characters, including space, tab(\t), and newline(\n) """
print isLower("F"),"\t", isLower1("F"),"\t", isLower2("F")
print isLower("f"),"\t", isLower1("f"),"\t", isLower2("f")
print isLower("adsadsad"),"\t", isLower1("adsadsad"),"\t", isLower2("adsadsad")

print string.whitespace