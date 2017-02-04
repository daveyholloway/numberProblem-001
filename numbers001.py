# Seamus Number Puzzle
#
# 
# Choose any 3 digit number (where each digit is different) e.g. 382 
# Write the digits biggest to smallest and smallest to biggest I.e. 832  and 238
# Subtract the smaller number from the bigger I.e. 832 - 238
# When you have your new number, reverse its digits and add these two numbers
# together I.e. 594 + 495
# 
# The number usually arrives at the answer 1089
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

    return(toNum(numList))

# Convert a number to a list
# Assume a 3 digit number
def toList(pNum):
    wNumList = []
    wNumList.append(pNum//100)
    wNumList.append((pNum - wNumList[0]*100)//10)
    wNumList.append((pNum - wNumList[0]*100 - wNumList[1]*10))

    return(wNumList)

# Convert a list to a number
# Assume a 3 digit number
def toNum(pNumList):
    return ((pNumList[0]*100) + (pNumList[1]*10) + pNumList[2])

# Sort
def sortNumFwd(pNum):
    return(toNum(sorted(toList(pNum))))

# Sort in reverse
def sortNumRev(pNum):
    return(toNum(sorted(toList(pNum), reverse=True )))

# Reverse a number
def reverse(pNum):
    wList = toList(pNum)
    wNum  = wList[0]
    wList[0] = wList[2]
    wList[2] = wNum
    return(toNum(wList))

# Let's start
# Print a few random numbers just to check the generator

for i in range(1,10):
    print('===================================================')
    myNumber = getRandomNumber()

    print('Starting with: ' + str(myNumber))

    print('Step 1 - Sort')
    print(' Sorted numbers: ' + str(sortNumFwd(myNumber)) + ", " + str(sortNumRev(myNumber)))

    print('Step 2 - Big minus Small')
    bigMinusSmall = sortNumRev(myNumber) - sortNumFwd(myNumber)
    print(' Answer: ' + str(bigMinusSmall))

    print('Step 3 - Reverse the answer')
    print(' Answer: ' + str(reverse(bigMinusSmall)))
    
    print('Step 4 - Add together')
    print(' Answer: ' + str(bigMinusSmall + reverse(bigMinusSmall)))

    if bigMinusSmall + reverse(bigMinusSmall) == 1089:
        print('Result: *** PASSED ***')
    else:
        print('Result: *** FAILED ***')

    print
    print
