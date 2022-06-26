#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import random      #brings a bunch of functions that could be used // this case the libray was imported
#import random as r  #now we can use a shorter name for the library instead of random just use r


#random.seed(1) # this is random looking
randInt = random.randint(0,10) # starts and ends start<=N<=end
print(randInt)

randFloat = random.random()  # 0.0 <=N<=1.0
print(randFloat)

randUniform = random.uniform(1,1100)  # starts and ends start<=N<=end
print(randUniform)

"""
randInt = r.randint(0,10) # starts and ends start<=N<=end
print(randInt)

randFloat = r.random()  # 0.0 <=N<=1.0
print(randFloat)

randUniform = r.uniform(1,1100)  # starts and ends start<=N<=end
print(randUniform)
"""