"""
###information from HW1 to summarize for user
Filename: songAttributeFunctions.py
Title: My favorite song, creating attribute functions.
The 3 attributes are Genre, Artist, and Year.
When the functions are called, it returns the variable
information of my favorite song.
Also for extta credit a boolean function was made that 
returns the opposite boolean of the parameter used.
###


Filename HW7: DictionairesAndSets.py
Refactor the code from HW1 about the favorite song.
Refactor so all the variables are held as dictionary keys
and values. Then refactor the print statments so that it's
a single loop that passes thru each time in the dictionary
and prints out it's key and then it's value.

extra credit:
Create a function that allows someone to guess the value of 
any key in the dictionary, and find out if they were right or
wrong. The function should accept parameters: Key and Value.
If the key and value are correct return True, all other cases
should return false.
"""


Dictionary = {"artist":"Phoenix","genre":"Indie Pop","year":"2000",}

def guessSongAttributes(key,value):
    if key in Dictionary:
        if value == Dictionary[key]:
            return True
    return False



for i in Dictionary:
    print(i,end=": ")
    print (Dictionary[i])


#extra credit
while(True): #True == True
    print("Uppercase and Lowercase is important in this check.")
    print("All keys are lower case. All values first leter of words are capitalized.")
    key = input("Enter Dictionary Key: \n")
    value = input("Enter Dictionary Value: \n")
    answer = guessSongAttributes(key,value)
    print(answer)
    if answer:
        continue
    else:
        break
        