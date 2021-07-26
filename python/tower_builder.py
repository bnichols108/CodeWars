# Description:
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# Tower block is represented as *
# Python: return a list
# Examples:
# tower_builder(1) -> ['*', ])
# tower_builder(2) -> [' * ', '***'])
# tower_builder(3) -> ['  *  ', ' *** ', '*****'])

def tower_builder(n_floors):
    # Creation of empty list variable to return at end of function.
    returnList = []
    # Creation of int variable to count spaces around the * for each floor.
    numOfSpaces = 0

    # For loop to iterate through the number of floors. Reversed the order to begin at the end to help keep track of
    # spaces. Also added +1 to the n_floors so that the range worked properly.
    for i in reversed(range(1, n_floors+1)):
        # If conditional to check if we're on the 1st floor.
        if i == 1:
            # If we're on the first floor, then no more floors to work on. Thus return
            # return is adding a list to the returnList that will have padding around the * for appropriate number of
            # spaces required depending on number of floors (n_floors). Also incorporating the [::-1] to reverse the
            # list.
            return (returnList + [(" " * numOfSpaces) + ("*") + (" " * numOfSpaces)])[::-1]
        else:
            # If we're not on the first floor, then add a list to returnList of the number of required * dependent upon
            # what floor we're on, including the appropriate number of spaces dependent upon the number of floors
            # (n_floors).
            returnList = returnList + [(" " * numOfSpaces) + ('*' * (i + (i - 1))) + (" " * numOfSpaces)]
            # Increment numOfSpaces to help keep track of padding required around subsequent *.
            numOfSpaces += 1