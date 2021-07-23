# Description:
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    # Create empty string
    numString = ""
    # For loop to iterate through the newly created list from the num variable
    for x in list(map(int,str(num))):
        # Concatenate the numString variable with the latest square of x
        numString = numString + str(x*x)
    # Return numString as an integer
    return int(numString)