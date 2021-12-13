# coding=utf-8


example = int(raw_input("Example number:"))

if example == 1:
    tupA = (1, "apple", 6.00)
    tupB = (tupA, "MIT", [4, 5])

    print "tupA is", tupA, "with length:", len(tupA)
    print "tupB is", tupB, "with length:", len(tupB)

    print "\nIndexing operations:"
    print "tupA[0] is:", tupA[0]
    print "tupA[2] is:", tupA[2]
    # print "tupA[3] is:", tupA[3] #Error - why?  #IndexError: tuple index out of range
    print "tupA[-1] is", tupA[-1]
    print "tupB[0][1] is", tupB[0][1]
    """tupB is a two-dimensional tuple"""
    print "\nSlicing operation."
    print "tupA[0:1] is ", tupA[0:1]
    print "tupA[0:100] is ", tupA[0:100]
    # tupA[0:100] is  (1, 'apple', 6.0)
    print "tupA[0:2] is ", tupA[0:2]
    print "tupA[:2] is ", tupA[:2]
    print "tupA[1:] is ", tupA[1:]
    print "tupA[:] is ", tupA[:]
    print "tupB[-1:-3] is ", tupB[-1:-3]
    # tupB[-1:-3] is  ()

    # Iteration through tuple
    print "\nIteration through tupB"
    """Use command+/ to comment quickly"""
    # for item in tupB:
    #     print item, "is of type", type(item)

    for i in tupB:
        print i, "is of type", type(i)

    # this is equivalent to
    print "\nIteration through tupB:"
    for i in range(len(tupB)):
        print tupB[i], 'is of type', type(tupB[i])

    """iteration: Repeated execution of a set of statements using either a recursive function call or a loop."""

    listA = [0, 1, 2]
    listA.append(3)
    print 'listA is', listA
    listA.remove(3)
    print 'listA is', listA

    listEmpty = [[]] * 10
    print listEmpty

    # instantiate: To create an instance of a class.
    # instance: An object that belongs to a class.
    listTenZero = [0] * 10
    print 'list of ten zero is ', listTenZero

    # Use iteration to check each of type of object in the listEmpty
    for item in listEmpty:
        print item, "is of type", type(item)

    # list: A named collection of objects, where each object is identified by an index.

    print "\n Matrix"
    # create a matrix
    M = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print M
    print M[2]
    print M[2][1]  # Access 3 in the 2,3 box

    #   Example 3: List operations
if example == 3:
    LA = [6.00, "MIT", 600, 600]

    for i in LA:
        print i, "is the type of ", type(i)

    LA.append("Harvard")  # The append method works on lists but not, of course, tuples.
    print LA
    LA.append(["Yale", "Standford"])
    # if the string contains a single quote (or an apostrophe, which is the same character), you have to use double
    # quotes to enclose it.
    print LA

    LA.pop()  # pop off the latest element
    print LA
    LA.pop(0)  # pop off element at index 0
    print LA

    """pop: Remove and return an item from the stack. The item that is returned is always the last one that was 
    added. """

    LA.extend(["Yale", "Stanford"])  # It's going to combine those lists.
    print LA

    """Q: Why we didn't have these methods for tuples"""
    # A: They're immutable

    LA.remove(600)
    print LA

    # LA.remove(500)     # Error
    if 500 in LA:
        LA.remove(500)

    LA.sort()
    print LA

    tupleA = (1, 2)
    tupleB = (3, 4)
    tupleC = tupleA + tupleB
    print tupleC  # That concatenates
if example == 4:
    tupA = (1, "apple", 6.00)

    listA = [0.234, "apple", (1, 2), 77]
    listB = [listA, "MIB", [3, 1, 4]]

    # Since tuples are immutable, cannot reassign
    # tupA[0] = 3 # This gives an error

    print "listA is: ", listA
    print "listB is: ", listB
    listA[0] = 88
    print "Now listA is: ", listA

    # Aliasing: giving two names to the same list - printing the same list
    """aliases: Multiple variables that contain references to the same object."""
    listX = [1, 4, 5]
    listY = listX
    print "listX is ", listX, "and listY is ", listY
    listX[0] = "banana"
    print "listX is ", listX, "and listY is ", listY

    # Aliasing happens when we define a list (lile listA,....."
    print "listB is now ", listB

    # To copy without aliasing use a full slice

if example == 5:  # Covert tuple to list & list to tuple
    test_tuple = (1, 4, "apple", "single")
    print "test_tuple is ", test_tuple

    tuple_into_list = list(test_tuple)
    tuple_into_list[3] = "banana"
    # test_tuple = tuple(tuple_into_list)
    test_tuple = tuple([1, 3, 4])
    print "now test_tuple is ", test_tuple
    print "     which is at type", type(test_tuple)
if example == 6:  # dictionaries
    staff = {'jiahao wu': 'jiahao.wu@asu.edu',
             'tianyuan xu': 'tianyuan.lu@asu.edu',
             'xuping lu': 'xuping.lu@asu.edu'}
    print len(staff)

    # Made a mistake! Fix Tianyuan's address
    staff['tianyuan xu'] = 'tianyuan.xu@asu.edu'
    # Add haonan chen
    staff['haonan chen'] = 'haonan.chen@asu.edu'
    print staff

    if "haonan chen" in staff:
        print "haonan chen is in the staff list"
    if 'xintao lin' not in staff:
        print 'Adding xintao to the staff list....'
        staff['xintao lin'] = 'xintao.lin@asu.edu'

    # Can't check for values with the 'in' keyword.
    print staff
    print "jiahao.wu@asu.edu" in staff
    # return False in console
    # The keys should be an immutable object.
    '''Example, we can use string and tuple as key, but not list as key'''
    # Key is going to be unique
    staff.keys().sort()  # Call the keys and sort the keys
    # Doesn't work. it's not sort by alphabetic order.
    '''Chaining method，call two methods'''
    print staff
    keys = staff.keys()  # Getting a list of keys.
    print "staff.keys() is ", keys
    keys.sort()  #
    print "keys.sort() is ", keys
    # go iteration
    for k in keys:
        print k, staff[k]

    # Oops, we fired Xintao lin!
    del staff['xintao lin']
    print staff

    # go through key, value pairs
    for TA, Email in staff.items():
        print 'TA', TA, " can be contacted at ", Email  # Return key-value pairs

#   Example 7: Recursion
if example == 7:
    # How might we make a factorial function?
    def factorial(n):
        # if [base case is true] - what is the base case?
        if n == 0:  # only one value for your base case.
            # 0! is 1
            return 1
        else:
            return n * factorial(n - 1)


    # Test!
    print factorial(0)  # Always check your base-case first.
    print factorial(5)


    # Can you write this using while loop.

    #   fibonacci

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)


    for i in range(10):
        print fibonacci(i)

    print fibonacci(0)
    print fibonacci(1)
    print fibonacci(5)


    def rec_exponentiation(b, e):
        if e == 0:
            return 1
        else:
            return b * rec_exponentiation(b, e - 1)


    '''Why we have only one base-case here'''
    # Accessing only one previous series

    # Test!
    print rec_exponentiation(3, 0)
    print rec_exponentiation(3, 2)


    # recursive multiplication
    def rec_multi(a, b):
        if b >= 0:
            if b == 0:
                return 0
            elif b == 1:
                return a
            else:
                return a + rec_multi(a, b - 1)
        else:
            return False


    # Test!

    print rec_multi(3, 0)
    print rec_multi(3, 1)
    print rec_multi(3, 5)
    print rec_multi(3, -5)


    def rec_multiplication(a, n):
        if n == 0:
            return 0
        elif n == 1:
            return a
        elif n == -1:
            return -a
        elif n > 1:
            return a + rec_multiplication(a, n - 1)
        else:
            return -a + rec_multiplication(a, n + 1)


    # Test!
    print rec_multiplication(3, 0)
    print rec_multiplication(3, 1)
    print rec_multiplication(3, -1)
    print rec_multiplication(3, 5)
    print rec_multiplication(3, -5)

# EXAMPLE 7 : Recursion

if example == 9:
    # Hanoi example
    def hanoi(n, s, t, b):
        assert n > 0
        if n == 1:
            print 'move ', s, ' to ', t
        else:
            hanoi(n - 1, s, b, t)
            hanoi(1, s, t, b)
            hanoi(n - 1, b, t, s)


    print hanoi(3, "Source", "Target", "Buffer")


    for i in range(1, 5):
        print "New Hanoi Example: hanoi (", i, " , source, target, Buffer"
        print "_____________________________"
        hanoi(i, "Source", "Target", "Buffer")


    def Hanoi(n, f, t, s):
        if n == 1:
            print 'move from ', f, ' to ', t
        else:
            Hanoi(n - 1, f, s, t)
            Hanoi(1, f, t, s)
            Hanoi(n - 1, s, t, f)
