"""Script will ask the user for two angles 
and retuns the angle with the smaller sin (magnitude)
"""

import math

def smaller_num(a, b):
    """ returns the smaller of a and b"""
    if a < b:
        return a
    else:
        return b

def smaller_sin(a, b):
    """ returns the number whos abs(sin) is smaller"""
    
    if abs(math.sin(a)) < abs(math.sin(b)):
        return a
    else:
        return b
    
# ask the user to enter two number
a = float(input("Enter first angle\t"))
b = float(input("Enter a second angle\t"))

print("the angle with the smaller sin magnitude is ", smaller_sin(a, b))