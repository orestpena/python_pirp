
"""

Create a function that takes 2 parameters: rows and columns (both are integers).
The functions should draw a playing board. After it's done being drawn return
True. For extra credit try to determine max width & height that your terminal &
screen can comfortabley fit w/o wrapping. If someone passes a value greater
than maximum return false.

"""

# / /  0
#----- 1
# / /  2
#----- 3
# / /  4
rowNumber = 5
columnNumber = rowNumber + 1

def rowsAndColumns(rows,columns):
    for row in range(rows): #0,1,2,3,4
        if row % 2 == 0:#0,2,4
            for column in range(1,columns):#1,2,3,4,5
                if column % 2 == 1:
                    if column != rows:
                        print(" ",end="")#1,3
                    else:
                        print(" ")#5
                else:
                    print("|",end="")#2
        else:#1,3
            for row in range (rows):
                print("-",end="")
            print("")
    return True

def horizontalVerticalCheck(h,v):
    return h != v

def chooseGreaterH(h,v):
    return h > v
        #return True

def chooseGreaterV(h,v):
    return v > h
        #return True

def checkDivThree(h):
    return h%3 != 0

def screenSize(horizontal,vertical):
    if horizontalVerticalCheck(horizontal,vertical):
        if chooseGreaterH(horizontal,vertical):
            vertical = horizontal
        if chooseGreaterV(horizontal,vertical):
            horizontal = vertical
    if checkDivThree(horizontal):
        #findDivNumber(horizontal)
        while True:
            horizontal = horizontal + 1
            if horizontal%30 == 0:
                break
    return horizontal
            

def bigRowsAndColumns(rows,columns,rNumber,cNumber,cDoubleNumber,horizontal,vertical):
    primenumber=rNumber
    columnNumber = cNumber
    for row in range(rows): #0,1,2,3,4
        #print(number)
        if row !=  rNumber:#0,2,4
            for column in range(1,columns):#1,2,3,4,5
                if column != columnNumber:
                    if column != rows:
                        print(" ",end="")#1,3
                    else:
                        print(" ")#5
                else:
                    print("|",end="")#2
                    if columnNumber == cNumber:
                        columnNumber = cDoubleNumber
                    else:
                        columnNumber = cNumber
            #print(" | | ")
            #     "12345"
        else:#1,3
            #if rows%modNumber == 0:
            for row in range (rows):
            #print("-----")
                print("-",end="")
            print("")
            rNumber = rNumber + primenumber
            #print(number)
    if horizontal > 180:
        return False
    if vertical > 180:
        return False
    return True

# Function being called to make a board game
drawn = rowsAndColumns(rowNumber,columnNumber)      
print(drawn)


# User can enter values for horizontal and vertical if greater than 180 will return false
# horizontal and vertical should be the same to get a symetrical playing board.
# setting horizontal == vertical, but user can change it.
# Also the board should be created using multiples of 3.

horizontal = 180
vertical = 180

# extra credit
horizontal = screenSize(horizontal,vertical)
vertical = horizontal
bigRowNumber = vertical
rNumber = bigRowNumber/3   #rowNumber
bigColumnNumber = horizontal + 1  
cDoubleNumber = horizontal*2/3   #columnDoubleNumber
cNumber = horizontal/3  #columnNumber

bigDrawn = bigRowsAndColumns(bigRowNumber, bigColumnNumber,rNumber,cNumber,cDoubleNumber,horizontal,vertical)
print(bigDrawn)