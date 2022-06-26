#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from random import random
from time import perf_counter, process_time

randVal = random() # 0.0<=N<=1.0
print(randVal)

upper = 1.0
lower = 0.0

#guess = 0.5
#startTime = perf_counter()
startTime = process_time()
while(True):
    guess = (upper + lower)/2
    if guess == randVal:
        break
    elif guess < randVal:
        #print("guess too low")
        lower = guess
    else:
        #print("guess to high")
        upper = guess
    #print("guess:",guess)
    #print("randVal:",randVal)
#    guess = (upper + lower)/2
#endTime = perf_counter()
endTime = process_time()
print(guess)
print("It took us:",endTime-startTime)
    

