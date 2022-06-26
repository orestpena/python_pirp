#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import time
#from time import *
# using the function clock wwas deprecated in 3.7
# https://docs.python.org/3.7/library/time.html#time.clock

#currentTime = time.process_time()
currentTime = time.perf_counter()
#currentTime = perf_counter()
print("Hello")
print("World")
#pastTime = time.process_time()
pastTime = time.perf_counter()
#pastTime = perf_counter()
print(pastTime - currentTime)

print("1")
time.sleep(3)
#sleep("3")
print("2")

for i in range(1,11):
    print(i)
    time.sleep(i)
    #sleep(i)