# Classes and Object
import math


class point:
    pass


blank = point()

blank.x = 3.0
blank.y = 4.0

print blank.x * blank.y

print "The type is", type(blank)
string1 = str(blank)
print string1[28:int(len(string1) - 1)]
print int(string1[28:int(len(string1) - 1)], 16)
print id(blank)
print blank
print hex(id(blank))


# print int('0x7f276d8c6638',16)

def printPoint(p):  # input an instance as argument
    print '(' + str(p.x) + ',' + str(p.y) + ')'
    print '(', str(p.x), ',', str(p.y), ')'


printPoint(blank)


# Example of 5.2

# def distance(x1,y1,x2,y2):
#     dx = x2 -x1
#     dy = y2 -y1
#     dsquard = dx**2 + dy**2
#     result = math.sqrt(dsquard)
#     return result
#
#
# print distance(10,2,3,5)

class distance():
    pass


point1 = distance()
point2 = distance()

print point1 is point2

print point1
print

point1.x = 2
point1.y = 2
point2.x = 2
point2.y = 2
# point2 = point1

print "point1 is shallow equity with point2:", point1 is point2


def distance1(point1, point2):
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    dsquard = dx ** 2 + dy ** 2
    result = math.sqrt(dsquard)
    return result


print distance1(point1, point2)


# Deep equality

def samePoint(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)


print samePoint(point1, point2)


class Time:
    pass



time = Time()
time.hours = 11
print "The type of time.hours is", type(time.hours)
time.minutes = 59
time.seconds = 30

"""the first operand is the format string, and the second operand is a tuple of expressions """
print "%d:%d:%d" % (time.hours,time.minutes,time.seconds)

t1 = Time()
t2 = Time()

t1.hours = 11
t2.hours = 11

t1.minutes= 40
t2.minutes= 30

t1.seconds= 29
t2.seconds= 30

def after(t1,t2):
    if t1.hours < t2.hours:
        return True
    elif t1.hours == t2.hours:
        if t1.minutes < t2.minutes:
            return True
        elif t1.minutes == t2.minutes:
            if t1.seconds < t2.seconds:
                return True
            elif t1.seconds == t2.seconds:
                print "It's the same time"
                return
            else:
                return False
        else:
            return False

    else:
        return False


def addTime(t1,t2):
    sum = Time()
    sum.hours = t1.hours + t2.hours
    sum.minutes = t1.minutes + t2.minutes
    sum.seconds = t1.seconds + t2.seconds
    return sum.hours,sum.minutes,sum.seconds


print after(t1,t2)
print addTime(t1,t2)