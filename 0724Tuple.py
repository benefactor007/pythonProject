# Chapter 9.Tuple

import random
import string

def demoTuple():
    tuple = "a", "b", "c", "d", "e", "f"
    tuple2 = ("a", "b", "c", "d", "e", "f")

    t1 = ("a",)
    t2 = 'b',
    t3 = 'c'
    """To create a tuple with a single element, we have to include the final comma:"""
    print "The type of t2 is ", type(t2)
    print "The type of t2 is ", type(t3)

    """In other words, strings are immutable and lists are mutable."""
    # a tuple that is similar to a list except that it is immutable

    print "The tuple[0] is ", tuple[0]
    print "The slice, tuple[:3] is ", tuple[:3]

    tuple = ('A',) + tuple[1:]
    print "Now the tuple is ", tuple


demoTuple()


def demoTupleAssignment():
    """swap the values of two variables in list"""
    list2 = ["a", "b", "c", "d", "e", "f"]

    temp = list2[0]
    list2[0] = list2[1]
    list2[1] = temp

    """There is an easy way to swap two element in list by using the Tuple Assignment"""

    print "Now the list2 is ", list2
    """ swap the values of two variables in Tuple"""

    # Python provides a form of tuple assignment that solves this problem neatly:
    #
    # >>> a, b = b, a
    list2[0], list2[1] = list2[1], list2[0]
    print "Now the list2 is ", list2


demoTupleAssignment()


def swap1(x, y):
    return y, x


"""It might be a wrong way to  """
# def swap2(x, y):
#     print "before x is", x
#     print "before x id is", id(x)
#     print "before y is", y
#     print "before y id is", id(y)
#     x, y = y, x
#     print "after x is ", x
#     print "after x id is", id(x)
#     print "after y is ", y
#     print "after y id is", id(y)


"""That's working, we accept the list as argument"""


def swap2(L, x, y):
    print "before x is", x
    print "before x id is", id(x)
    print "before y is", y
    print "before y id is", id(y)
    print "before L[x] is ", L[x]
    print "before L[x] id is", id(L[x])
    print "before L[y] is ", L[y]
    print "before L[y] id is", id(L[y])
    L[x], L[y] = L[y], L[x]
    print "after L[x] is ", L[x]
    print "after L[x] id is", id(L[x])
    print "after L[y] is ", L[y]
    print "after L[y] id is", id(L[y])


def swap(L, x, y):
    temp = L[x]
    L[x] = L[y]
    L[y] = temp


list = ["a", "b", "c", "d", "e", "f"]


# list[0],list[1] = swap1(list[0],list[1])

# swap2(list,0,1)
# print list

def demoRandomNumbers():
    for i in range(10):
        x = random.random()
        print x


def generateRandomNum(low, high):
    # x = 0
    if 0.0 < low < 1.0 and 0.0 < high < 1.0:
        while True:
            x = random.random()
            if low <= x <= high:
                return x


# demoRandomNumbers()
print "The random num between 0.1 and 0.2", generateRandomNum(0.1, 0.2)
print "The random num between 0.8 and 0.9", generateRandomNum(0.8, 0.9)
print "The random num between 0.0 and 0.1", generateRandomNum(0, 0.1)
print "The random num between 1 and 2", generateRandomNum(1, 2)
# print "The random num between 1 and 1", generateRandomNum(1, 1)


print "to generate a random integer between 1 and 10, the num is ", random.randint(1, 10)
print "to generate a random integer between 10 and 10, the num is ", random.randint(10, 10)
print "to generate a random integer between 0 and 0, the num is ", random.randint(0, 0)
print "to generate a random integer between -5 and -1, the num is ", random.randint(-5, -1)


def randomList(n):  # input the size of List
    s = [0] * n
    for i in range(n):
        s[i] = random.random()
    return s

def redprint(str):
    return "\033[4;31m"+ str + "\033[0m"

L = [-1,'3','4']
for i in range(len(L)):
    print redprint(str(L[i])), '\t',


def inBucket(t,low,high):
    count = 0

    for num in t:
        if low < num < high:
            #print "num is ", num, "and type of n is ", type(num)
            #print "index is ", t.index(num), "and type of n is ", type(t.index(num))

            count += 1

    return count

def demoListOfRandomRum():
    print randomList(8)
    L = randomList(10)
    #print "The L is ", L
    #print "The count num. between 0.1 and 0.5 is ", inBucket(L, 0.1, 0.5)
    # low = inBucket(L, 0.0, 0.5)
    # high = inBucket(L,0.5,1.0)
    # print "The low is", low
    # print "The high is", high

    # numBuckets = 10
    # bucket = [0] * numBuckets
    # bucketWidth = 1.0 / numBuckets
    # for i in range(numBuckets):
    #     low = i * bucketWidth
    #     high = low + bucketWidth
    #     #print low, "to", high
    #     bucket[i] = inBucket(L, low, high)
    # print bucket

    numBuckets = 10
    buckets = [0] * numBuckets
    print "The list is", L
    for i in L:
        print "the i is ", i
        index = int(i*numBuckets)
        print "the index is", index
        buckets[index] += 1
        print "the bucket[",index,"] is ", buckets[index]


demoListOfRandomRum()

L = randomList(10000)
def histogram(L,num): # input list and number of bucket
    bucket = [0] * num
    for i in L:
        index = int(i*num)
        bucket[index] += 1
    return bucket

def oldhistogram(L,num):
    bucketwide = 1.00/num
    bucket = [0]*num
    for i in range(num):
        low = i*bucketwide
        high = low + bucketwide
        bucket[i] = inBucket(L, low, high)
    return bucket

print histogram(L,10)
print oldhistogram(L,10)