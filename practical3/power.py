#!/usr/bin/python

## Each function should print out a result
## square is calculated length * length
## cube is calculated length * length * length
## hypercube is calculated length * length * length * length

def square (x):
    return x**2

def cube (x):
    return square (x)*x

def hypercube(x):
    return cube (x)*x

def power (x, n):
    if n == 1:
        return x

    return x * power (x, n-1)

    '''if n == 1:
        return x
    elif n == 2:
        return x * power(x, 1)
    elif n == 3:
        return x * power (x, 2)
    elif n == 4:
        return x * power (x, 3)
'''

    '''if n == 1:
        return x
    elif n == 2:
        return square (x)
    elif n == 3:
        return cube (x)
    elif n == 4:
        return hypercube (x)
    '''



length=6
square(length)
cube(length)
hypercube(length)

# Task 5
print "The square of", length, "is:", square(length)
print "The cube of", length, "is:", cube(length)
print "The hypercube of", length, "is", hypercube(length)

# Task 6
print "The square of", length, "is:", power (length,2)
print "The cube of", length, "is:", power (length, 3)
print "The hypercube of", length, "is", power (length, 4)
