# Description:
# You might know some pretty large perfect squares. But what about the NEXT one?
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is
# non-negative.
# Examples:
# find_next_square(121) --> returns 144
# find_next_square(625) --> returns 676
# find_next_square(114) --> returns -1 since 114 is not a perfect square

import math

def find_next_square(sq):
    # Set num variable by calling the math.sqrt function of sq
    num = math.sqrt(sq)

    # If conditional to confirm whether num is a perfect square
    if int(num)**2 == sq:
        # Since num is perfect square, return the next perfect square
        return int(((num+1)**2))
    else:
        # Since num is not a perfect square, return -1
        return -1