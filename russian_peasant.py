__author__ = 'Anastasiya'
import math
from random import randrange
import time

def multiplier(a, b):
    sign = 1
    if a < 0:
        sign = -1
        a = -a
    if b < 0:
        sign = -sign
        b = -b
    sum = 0
    while a >= 1 or a <= -1:
        #print(a)
        if a % 2 != 0:
            sum = sum + b
        a = int(a / 2)
        #a = math.floor(a)
        #print(a)
        b = b * 2
        #print(b)

    return sum * sign

#print(int(-2.5/2))
#print(multiplier(600, 800))

#print(600*800)
"""for i in range(1, 100):
    start_time = time.time()
    a = randrange(-500000, 500000)
    b = randrange(-500000, 500000)
    if multiplier(a, b) != a*b:
        print("Do NOT pass" + " iteration  " + str(i) + " " +
               str(a) + " " + str(b))"""

def test_alg():
    a = randrange(-500000, 500000)
    b = randrange(-500000, 500000)
    start_time = time.time()
    print(multiplier(a, b))
    print("Algorithm took %f seconds" % (time.time()-start_time))
    assert multiplier(a, b) == a*b

test_alg()
