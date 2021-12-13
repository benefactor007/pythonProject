# coding=utf-8
# Hint
def demoHint():
    previous = {0: 1, 1: 1}

    def fibonacci(n):
        if previous.has_key(n):
            return previous[n]
        else:
            newValue = fibonacci(n - 1) + fibonacci(n - 2)
            previous[n] = newValue
            return newValue

    print previous
    print fibonacci(2)
    print fibonacci(4)
    print previous
    print fibonacci(40)
    print fibonacci(50)
    print fibonacci(60)

    print type(1L)
    print long(1)
    print long(2.2)
    print long('57')


def demoCountingLetter():
    def countingLetter():
        letterCount = {}
        for letter in "Mississippi":
            letterCount[letter] = letterCount.get(letter, 0) + 1
            print "The letter ", letter, "is", letterCount[letter]
        return letterCount

    def adCountingLetter(dict):  # input dict. as argumeent
        dictItem = dict.items()
        dictItem.sort()
        return dictItem

    print adCountingLetter(countingLetter())
    print countingLetter()


###Start to learn Files and exceptions

f = open("test.dat", "w")
print f
f.write('Now is the time')
f.write('to close the file')
f.close  # Closing the file tells the system that we are done writing and makes the file available for reading.
f = open("test.dat", "r")
try:
    f = open("test.cat", "r")
except Exception:
    print 'We got a error'

text = f.read()
print text
f = open("test.dat", "r")
print f.read(5)
print f.read(1000006)  # if not enough characters are left in the file, read returns the remaining characters.
print f.read()
f = open("test.dat", "r")
print f.read()


def copyFile(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while True:
        text = f1.read(50)
        if text == "":
            break
        f2.write(text)

    f1.close()
    f2.close()
    return


copyFile("test.dat", "test1.dat")
f = open("test1.dat", 'r')
print f.read()


# To demostrate,

def demoFilterFile():
    def redprint(str):
        return "\033[31m" + str + "\033[0m"

    f = open("test.dat", "w")
    f.write("line one \nline two\nline three\n")
    f.close()
    f = open("test.dat", "r")
    print f.read()
    f.close()
    f = open("test.dat", "r")
    print "The readline method shows ", f.readline()
    print "The", redprint("readlines"), "medthod shows ", f.readlines()
    print "To continue, we print f.readlines()", f.readlines()

    def filterFile(oldFile, newFile):
        f1 = open(oldFile, "r")
        f2 = open(newFile, "w")
        while True:  # The while loop is infinite
            text = f1.readline()
            print "This line shows", text

            if text == "":
                break
            if text[1] == "#":
                continue
            f2.write(text)

        f1.close()
        f2.close()
        return

    f = open("test.dat", "w")
    f.write("#123\n")
    f.write("#jojo\n")
    f.write("#321\n")
    f.close()
    f = open("test.dat", "r")
    print f.read(1)
    print "The f.read(0) is ", f.read(0)
    f.close()

    filterFile("test.dat", "filter1.dat")
    f = open("filter1.dat", "r")
    print "The content of filter1 is "
    print f.read()


# To demostrate, writing variable.
def readFile(filename):
    f = open(filename, "r")
    print f.read()
    return f.close()


"""if we want to put other values in a file, we have to convert them to strings first"""
f = open("test2.dat", "w")
x = 52
f.write(str(x))
f.close()
readFile("test2.dat")

cars = 52
cars = "%d" % cars

"""the first operand is the format string, and the second operand is a tuple of expressions """

print "The type of car is ", type(cars)
cars = 52
print "In July we sold %d cars" % cars

"""the format sequence "%f" formats the next item in the format string, so we can embed a value in a sentence"""

# embed əmˈbed fix (an object) firmly and deeply in a surrounding mass.

print "In %d days we made %f million %s." % (34, 6.1, 'dolloars')

try:
    "%d %d %d" % (1, 2)
except Exception:
    print 'We got a error'

try:
    "%d" % 'dollars'
except Exception:
    print 'We got a error'

"""We can specify the number of digits as part of the format sequence"""
print "%6d" % 62
print "%12f" % 6.1
"""The number after the percent sign is the minimum number of spaces the number will take up"""
print '%-6d' % 62
print '%12.2f' % 6.112  # the result takes up twelve spaces and include two digits after the decimal


def report(wages):  # input dict as argument, wages = tuition
    students = wages.keys()
    students.sort()
    for student in students:
        print "%-20s %12.2f" % (student, wages[student])


wages = {"JOJO": 10000.5, "Lu": 9999.99, "Dynasty": 88888.8}
report(wages)

"""The file named test.dat resides in a directory named dict, which resides in Desktop, which resides in jnd"""
# f = open("/home/jnd/Desktop/test.dat","w")
# f.write("#123\n")
# f.close()
# #readFile("/home/jnd/Desktop/test.dat")
# f = open("/home/jnd/Desktop/test.dat", "r")
# print "The readline() is ", f.readline()
import pickle


def demoPickle():
    # pickle ˈpik(ə)l : a difficult or messy situation.
    f = open("test.pck", "w")
    # To store a data structure, use the dump,dəmp, mehtod
    pickle.dump(12.3, f)
    pickle.dump([1, 2, 3], f)
    f.close()

    f = open("test.pck", "r")
    x = pickle.load(f)
    print x
    print "the type of x is", type(x)
    y = pickle.load(f)
    print y
    print "the type of y is", type(y)
    try:
        z = pickle.load(f)
        print z
        print "the type of z is", type(z)
    except Exception:
        print "we got an error"


demoPickle()


def demoException():
    filename = raw_input('Enter a file name: ')
    try:
        f = open(filename, "r")
    except IOError:
        print 'There is no file named', filename


def exists(filename):
    try:
        f = open(filename, "r")
        f.close()
        return True
    except IOError:
        return False


print exists("123")


# demoException()


def inputNumber():
    x = input("Pick a number: ")
    try:
        if x == 17:
            raise ValueError('17 is a bad number')
    except Exception, e: # except Exception as e
        print e
    return x

"""For a variety of occasions. Other examples include TypeError, KeyError and NotimplementedError """
print inputNumber()
