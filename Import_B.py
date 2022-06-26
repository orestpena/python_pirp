#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import random as r  #now we can use a shorter name for the library instead of random just use r
                     #we imported the whole library, but could be a problem if you have memory constraints.
                     #so only import in certain features or what you need.

#from random import randint, random, uniform #from random you can use * which imports everything.
#from random import *   # have to be careful with the * b/c it could overwrite other functions

randInt = r.randint(0,10) # starts and ends start<=N<=end
print(randInt)

randFloat = r.random()  # 0.0 <=N<=1.0
print(randFloat)

randUniform = r.uniform(1,1100)  # starts and ends start<=N<=end
print(randUniform)

simpleList = [1,3,5,7,11]
pickElement = r.choice(simpleList)
print(pickElement)
print(simpleList)
r.shuffle(simpleList)  #randome shuffle was used to shuffle the list that was originally created
print(simpleList)