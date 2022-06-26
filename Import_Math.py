#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import math
# https://docs.python.org/3/library/math.html
#Val = 3
Val = 3.14

sqrtVal = math.sqrt(Val)
print(sqrtVal) # square ^2 == **2
#print(sqrtVal**2) # square ^2 == **2
# a limitation of the function doesn't get it back to 3 b/c of rounding errors, but close enough

expVal = math.exp(Val) #taking the exponential using euler's constant
print(expVal)

#factVal = math.factorial(Val) #5! = 5*4*3*2*1 
#
#print(factVal)
factVal = math.factorial(math.floor(Val)) #5! = 5*4*3*2*1 
print(factVal)

sinVal = math.sin(Val)
print(sinVal)

floorVal = math.floor(Val)
print(floorVal)

ceilingVal = math.ceil(Val)
print(ceilingVal)