# Hw4 make a unique list.
# If the value doesn't exist add it and return True.
# If it does exisit don't add it and return False.
myUniqueList = []
myLeftovers = []

def addToList(item):
    if item not in myUniqueList:
        myUniqueList.append(item)
    else:
        myLeftovers.append(item)    


addToList("apple")
print(myUniqueList)
print(myLeftovers)
addToList("apple")
print(myUniqueList)
print(myLeftovers)
addToList("orange")
print(myUniqueList)
print(myLeftovers)
addToList("avocado")
print(myUniqueList)
print(myLeftovers)
addToList("banana")
print(myLeftovers)
addToList("orange")
print(myUniqueList)
print(myLeftovers)
addToList("mango")
print(myUniqueList)
print(myLeftovers)
addToList("avocado")
print(myUniqueList)
print(myLeftovers)
addToList("strawberry")
print(myUniqueList)
print(myLeftovers)
addToList("grape")
print(myUniqueList)
print(myLeftovers)
addToList("strawberry")
print(myUniqueList)
print(myLeftovers)
addToList("avocado")
print(myUniqueList)
print(myLeftovers)
addToList("strawberry")
print(myUniqueList)
print(myLeftovers)