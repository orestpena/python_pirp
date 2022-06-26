#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# This program performs examples

#float("123.4") - > 123.4
#float("N/A") - > error

#keyWord = "123"
keyWord = "Hello"

#print(int(keyWord))   #used to determine what type of error it produces, ValueError
try:
    raise NameError("Error") # this will pass the string to the exception
    #raise NameError # this will go into our other exception (user raise error)
    #raise ValueError # this will go into our value error. raise are user defined instead of the computer
    #print(int(keyWord))
    #print(int("Hello"))
#except:
#    #print("Entered exception")
#    pass # if it goes into a fail, it does nothing and just passes
#except Exception as e:
#    print(str(e))

except ValueError:
    print("got a ValueError")

#except:
#    print("Other type of exception")
    #raise # this is a way to manually handle a user crash

except Exception as e:
    print("Other type of exception")
    print(str(e))

finally:
    print("finally")

# you can have mutliple exceptions by they have to follow each other one by one
# you can't include other things such as while or if statements etc.
# in try except, there is a finally keyword.
# we do all the error handling and checks and at the end we finally do this
# only use the finally if you need it

print("Past exception")
