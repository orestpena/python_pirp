## HW3 Create a function that accepts 3 pararameters
# and determines if at least 2 are equal and send TRUE
# otherwise send FALSE.
# Extra Credit to compare strings and ints


# Function to check if 2 or more ints/strings are equal to each other
def compareThreeParameters(NumberOne, NumberTwo, NumberThree):
    if int(NumberOne) == int(NumberTwo) or int(NumberOne) == int(NumberThree) or int(NumberTwo) == int(NumberThree):
        return True
    else: 
        return False

## below are different testcases to verify the function worked as expected.

# check int/string - TRUE
Par1 = 6
Par2 = 5
Par3 = "5"

answer=compareThreeParameters(Par1, Par2, Par3)
print(answer)

# check string/int - TRUE
Par1 = "6"
Par2 = 5
Par3 = "6"

answer=compareThreeParameters(Par1, Par2, Par3)
print(answer)

# check all ints - TRUE
Par1 = 5
Par2 = 5
Par3 = 6

answer=compareThreeParameters(Par1, Par2, Par3)
print(answer)

# check all strings - FALSE
Par1 = "3"
Par2 = "2"
Par3 = "1"

answer=compareThreeParameters(Par1, Par2, Par3)
print(answer)

# check all strings - TRUE
Par1 = "4"
Par2 = "4"
Par3 = "6"

answer=compareThreeParameters(Par1, Par2, Par3)
print(answer)

# check all ints - FALSE
Par1 = 1
Par2 = 5
Par3 = 7

answer=compareThreeParameters(Par1, Par2, Par3)
print(answer)

# check strings - TRUE
Par1 = "3"
Par2 = "7"
Par3 = "7"

answer=compareThreeParameters(Par1, Par2, Par3)
print(answer)
