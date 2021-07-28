# Description:
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# Examples:
# Sam Harris => S.H
# Patrick Feeney => P.F

def abbrev_name(name):
    # Split up the string into a list by splitting it between the space
    wordList = list(name.split(" "))

    print(wordList)
    # Create the variable that will be returned. Create the variable via the first character of each object in the list
    # with a period in the middle
    abbreviation = (wordList[0][0] + "." + wordList[1][0])
    # Force the variable to be all uppercase
    abbreviation = abbreviation.upper()
    # Return the finished variable
    return abbreviation