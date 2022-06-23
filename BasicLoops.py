##HW#5 Basic Loops
# Fizz Buzz: writes a program that prints the numbers from 1 to 100
# But for mulitples of 3 print "Fizz" instead of the numbers and for the
# multiples of 5 print "Buzz". For numbers which are multiples of both
# 3 and 5 print "FizzBuzz"

def primeCheck(variable):
    counter = 0
    for test in range(1,variable+1):
        if (variable % test == 0):
            counter = counter + 1
    if (counter < 3):
        return True
    else:
        return False


for i in range(1,101):
    if(i % 3 == 0):
        if(i % 5 == 0):
            if(primeCheck(i)):
                print("FizzBuzz - Prime")
            else:
                print("FizzBuzz")
        else:
            if(primeCheck(i)):
                print("Fizz - Prime")
            else:
                print("Fizz")
    elif(i % 5 == 0):
        if(primeCheck(i)):
            print("Buzz - Prime")
        else:
            print("Buzz")
    else:
        if(primeCheck(i)):
            print("Prime")
        else:
            print(i)