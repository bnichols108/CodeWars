# Description:
# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early
# to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with
# a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings
# representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter
# (direction) and you know it takes you one minute to traverse one city block, so create a function that will return
# true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will,
# of course, return you to your starting point. Return false otherwise.
# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or
# 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).
# Examples:
# is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) -> True
# is_valid_walk(['n','s','n','s','n','s','n','s','n']) -> False
# is_valid_walk(['w'] -> False
# is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) -> False

def is_valid_walk(walk):
    # If conditional to check length of walk list. Since we can only walk 10 blocks and one direction is one block, that
    # means we must have a list of 10. If not, return False.
    if len(walk) != 10:
        return False

    # Create variables to count number of each direction for later comparison
    numN = 0
    numS = 0
    numE = 0
    numW = 0

    # For loop to iterate through the walk list for each character (direction)
    for direction in walk:
        # If conditionals to check for each direction and increment the count of correctly matched direction
        if direction == 'n':
            numN += 1
        elif direction == 's':
            numS += 1
        elif direction == 'e':
            numE += 1
        else:
            numW += 1

    # If conditional to compare directions. N and S directions must be same amount as well as E and W directions must be
    # the same amount. If they're different, we will not be back at the starting point.
    if (numN == numS) and (numE == numW):
        # If true, we're back at the starting point. Return True
        return True
    else:
        # If not true, we're not back at the starting point. Return False
        return False