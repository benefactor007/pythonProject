def rec_mult(m, n):
    # Base case (only occur if call the function)
    if n == 0 or m == 0:
        return 0
    elif n >= 1:
        return m + rec_mult(m, n - 1)
    elif n < 1:
        return -m + rec_mult(m, n + 1)

print "Test1 (base case ) : 0 x 1 = 0", rec_mult(0, 1)
print "Test1 (base case ) : 1 x 0 = 0", rec_mult(1, 0)
print "Test2 (n >= 1 ) : 9 x 8 = 72", rec_mult(9, 8)
print "Test3 (n < 1) : 3 x -2 = -6", rec_mult(3, -2)

# "It is not too intuitive right?"
# so if we implement it iteratively though, I think it's a little easier to understand.

def mult(m, n):

    if n == 0 or m == 0:
        return 0
    result = 0
    if n >= 1 :
        while n > 0:
            # result += m
            # n -= 1
            result = result + m
            n = n -1

    elif n <= 1 :
        while n < 0:
            # result -= m
            # n += 1
            result = result - m
            n = n + 1

    return result

print "Test1 (base case ) : 0 x 1 = ", mult(0, 1)
print "Test1 (base case ) : 1 x 0 = ", mult(1, 0)
print "Test2 (n >= 1 ) : 9 x 8 = ", mult(9, 8)
print "Test3 (n < 1) : 3 x -2 = ", mult(3, -2)
