import numpy as np
from numba import jit
from string import ascii_letters

print(ascii_letters)

def xrange(x):
    return iter(range(x))

@jit(nopython=True, nogil=True)
def commpute(maxLength):
    charList = '-=!@#$%^&*()1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz<>?,./:";'
    result = []

    for current in xrange(maxLength):
        a = [i for i in charList]
        for y in xrange(current):
            a = [x + i for i in charList for x in a]
        result = result + a


    print("End")
    return result