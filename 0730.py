# coding=utf-8
import copy


class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def after(self, time2):
        if self.hour > time2.hour:
            return 1
        if self.hour < time2.hour:
            return 0

        if self.minute > time2.minute:
            return 1
        if self.minute < time2.minute:
            return 0

        if self.second > time2.second:
            return 1
        if self.second < time2.second:
            return 0

    def printTime(time):
        print str(time.hour) + ":" + \
              str(time.minute) + ":" + \
              str(time.second)

    def convertToSecond(self):
        minute = self.minute + self.hour * 60
        second = minute * 60 + self.second
        return second

    def increment(self, second):
        seconds = self.convertToSecond() + second
        print "The seconds is", seconds
        return makeTime(seconds)


def makeTime(second):
    time = Time()
    time.hour = second / 3600
    time.minute = (second % 3600) / 60
    time.second = second % 60
    return time


currentTime = Time()
currentTime.hour = 9
currentTime.minute = 30
currentTime.second = 50

currentTime.printTime()

doneTime = Time()
doneTime.hour = 9
doneTime.minute = 50
doneTime.second = 50

if doneTime.after(currentTime):
    print "The bread is not done yet"

print "The type of currentTime is", type(currentTime)
print "The type of currentTime.printTime() is", type(currentTime.printTime())
print "The type of currentTime.convertToSecond() is", type(currentTime.convertToSecond())
print "The type of makeTime(currentTime.convertToSecond()) is", type(makeTime(currentTime.convertToSecond()))
# newTime = Time()
try:
    print "The type of newTime is", type(newTime)
except NameError, e:
    print e

newTime = copy.deepcopy(makeTime(currentTime.convertToSecond()))
print "The type of newTime is", type(newTime)
newTime.printTime()
print "The type of newTime.printTime()", type(newTime.printTime())

# t1 = Time()
# #t2 = Time()
#
# t1.name = "Tianyuan"
# t2 = copy.deepcopy(t1)
#
# print "The type of t2 is", type(t2)

print "The original doneTime is",
doneTime.printTime()
(doneTime.increment(500)).printTime()


def find(str, ch):
    for i in range(len(str)):
        if str[i] == ch:
            return i
    return False


print "find(\"apple\", \"p\") is ", find("apple", "p")
print "find(\"apple\", \"z\") is ", find("apple", "z")


##14.2 optional argument

def find1(str, ch, start=0):
    index = start
    while index < len(str):
        if str[index] == ch:
            return index
        index += 1
    return False


print "find1(\"apple\", \"p\") is ", find1("apple", "p", )
print "find1(\"apple\", \"p\", 1) is ", find1("apple", "p", 2)
print "find1(\"apple\", \"p\", 2) is ", find1("apple", "p", 3)


def find2(str, ch, start=0, end=-1):
    if -1 < end <= len(str):
        # if end <= len(str):
        length = end
    elif end == -1:
        length = len(str)
    else:
        return False

    index = start
    while index < length:
        if str[index] == ch:
            return index
        index += 1
    return False


print "find2(\"apple\", \"p\") is ", find2("apple", "p")
print "find2(\"apple\", \"p\") is ", find2("apple", "p", 0, 1)
print "find2(\"apple\", \"p\", 1) is ", find2("apple", "p", 2, 5)
print "find2(\"apple\", \"p\", 2) is ", find2("apple", "p", 3, 5)
# str2 = "banana"
# print str2[2:]
# print len(str2[2:])

# class Time:


currentTime = Time(9, 30)

currentTime.printTime()


#########14.7
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


currentPoint = Point()
print str(currentPoint)
"""If a class provides a method named __str__, it overrides the default behavior of the Python built-in str function"""
testPoint = Point(3, 4)
print "the type of testPoint is", type(testPoint)
print str(testPoint)

P = Point(6, 9)
print P

# 14.8 Operator overloading

p1 = Point(6, 9)
p2 = Point(9, 6)
p3 = p1 + p2
print "p3 is", p3
p4 = p1.__add__(p2)
print "p4 is", p3
print "p3 is p4？", (p3 is p4)

# As an exercise, add a method __sub__(self, other) that overloads the subtraction operator, and try it out.
p5 = Point(6,6)
p6 = Point(9,9)
p7 = p5 - p6
print "p7 is", p7