#def FunctionName(Input):
#   Action
#   return Output

def addOne(Number):
    Output = Number + 1
    return Output

Var = 0
print(Var)
Var2 = addOne(Var)
Var3 = addOne(Var2)
Var4 = addOne(2.1+3.4)
print(Var2)
print(Var3)
print(Var4)

def addOneAddTwo(NumberOne, NumberTwo):
    Output = NumberOne
    #Output = Output + NumberTwo + 2
    Output += NumberTwo + 2
    return Output

Sum = addOneAddTwo(Var2, Var3)

print(Sum)

def printmessage(message, ntimes =1):
    print(message * ntimes)
printmessage("Hello")
printmessage("Hello", 5)

