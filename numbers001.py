# Seamus Number Puzzle
#
# Modification History
# ====================
#
# When       Who             Why
# ========== =============== ===========================================
# 26/01/2017 Dave            Initial Version
#
import random

# A function to return a 3 digit random number with no repeating
# digits
def getRandomNumber():
    # declare an empty list
    numList = []
    # Keep going until we get 3 unique numbers in the list
    while len(numList) < 3 :
        # Generate a random number
        myNum = random.randint(0,9)
        # If it's not already in the list then add it, otherwise
        # try again
        if not (myNum in numList):
            numList.append(myNum)

    return((numList[0]*100)+(numList[1]*10)+numList[2])


# Let's start
# Print a few random numbers just to check the generator
for i in range(1,10):
    print(getRandomNumber())
