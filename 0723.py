# coding=utf-8
##List

##In this file, we encapsulate some code as function, which as follows,
# 1. demoRange()
# 2. isList(obj)
# 3. traversalList(list)
# 4.indexToList(int)
# 5.redprint(str)
# 6.demoObjectAndValues()
# 7.demoStringsAndLists()
# 8.strToList(str)
# 9.advTraversalList(list)
    #traversal

import string

def demoRange():
    print range(1, 10)
    print range(10)
    print range(1, 10, 2)
    vocabulary = ["ameliorate", "castigate", "defenestrate"]
    numbers = [17, 123]
    empty = []
    print vocabulary, numbers, empty

    horsename = ["war", "famine", "pestilence", "death"]
    ##pestilence ˈpestələns n. 瘟疫（尤指鼠疫）；有害的事物
    for i in range(len(horsename)):
        print horsename[i]

    doubleNestedList = ['spam!', 1, ["Brie", "Roquefort", "Pol le Veq"], [1, 2, 3]]
    tripleNestedList = [['spam!', [3, 4, 5]], 1, ["Brie", "Roquefort", "Pol le Veq"], [1, 2, 3]]
    traversalList(doubleNestedList)

    Name = "Jiahao Wu"

    # if type(testList) == list
    print "The type of list is ", type(doubleNestedList)
    print "Is it a list? The answer is ", isList(doubleNestedList)
    print "Is it a list? The answer is ", isList(Name)

    advTraversalList(doubleNestedList)
    advTraversalList(tripleNestedList)

    print "pestilence" in horsename
    print "debauchery" not in horsename

def demoTraversalNestedLists():
    tripleNestedList = [['spam!', [3, 4, 5]], 1, ["Brie", "Roquefort", "Pol le Veq"], [1, 2, 3]]
    print tripleNestedList
    advTraversalList(tripleNestedList)

def isList(obj):
    # obj means object
    # we use the built-in function, which is isinstance(), to determine whether the object is belong
    # to the type of latter.

    return isinstance(obj, list)


def advTraversalList(list):
    for i in range(len(list)):

        if isList(list[i]) == True:
            advTraversalList(list[i])
        else:
            print list[i], "\t",


def traversalList(list):
    for i in range(len(list)):
        print list[i]


def strToList(str):
    L = []
    for i in range(len(str)):
        L.append(str[i])
    return L

print strToList(string.lowercase)


#demoRange()
demoTraversalNestedLists()

def indexToList(int):
    L = []
    for i in range(int):
        L.append(str(i))  # str(), which convert the int to str base on decimal
    return L




def demoListDelete():
    a = ["one", "two", "three"]
    del a[1]
    print a

    print string.lowercase
    list = strToList(string.lowercase)

    # numList = []
    # for i in range(len(string.lowercase)):
    #     numList.append()
    print "The type of len(string.lowercase) is ", type(len(string.lowercase))
    print "The output of len(string.lowrcase is ", len(string.lowercase)

    print indexToList(len(string.lowercase))
    print strToList(string.uppercase)
    print "The next step, we do delete list[1:5}"
    del list[1:5]
    print list

    list = strToList(string.lowercase)
    print "The next step, we do slice list[1:5}"
    print list[1:5]


demoListDelete()

def redprint(str):
    return "\033[31m"+ str + "\033[0m"

def demoObjectAndValues():
    print "Every object has a unique " + redprint("identifier")
    #Use id() to identify the unique ID for the object as given.
    a = "banana"
    b = "banana"
    print "The id of a is ", id(a)
    print "The id of b is ", id(b)
    a = [1,2,3]
    b = [1,2,3]
    print "The id of a is ", id(a)
    print "The id of b is ", id(b)

demoObjectAndValues()

def demoStringsAndLists():
    song = "The rain in Spain..."
    print string.split(song)
    print "We use ",redprint("in"), " as the delimiter, which shows ", string.split(song, "in")
    #delimiter dēˈlimit
    list = ["The","rain","in","Spain"]
    print string.join(list)
    print "string.join(list, '\"_\"'）shows ", string.join(list,"_")
    print "sting.join(string.split(song)), the output as shown below"
    print string.join(string.split(song))
    print "The type of string.join function is ", type(string.join(string.split(song)))


demoStringsAndLists()

list = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
horsemen = ["war", "famine", "pestilence", "death"]
numberlist = ["1",["1","2","3","4","5","6","7"],"2","3","4","5","6","7"]
def exercise1(L):
    # As an exercise, write a loop that traverses the previous list and prints the length of each element. What
    # happens if you send an integer to len?
    """There is a TypeError: object of type 'int' has no len()"""
    i = 0
    while i < len(L):
        print len(L[i])
        i += 1


exercise1(numberlist)
