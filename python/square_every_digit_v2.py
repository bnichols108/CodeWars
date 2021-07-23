# After reviewing other users' solutions, I found that my solution is very close to the highly ranked one. But I need
# to tweak my code just a little

# 1. I found out that I can iterate through a string, so there's no need to force num to become a list. Because of that,
#    I will leave num as a string.
# 2. I also did think about utilizing the += assignment operator but never put it in place. I will use it in this latest
#    version.

def square_digits(num):
    # Create empty string
    numString = ""
    # For loop to iterate through the num string
    for x in str(num):
        # Concatenate the numString variable with the latest square of x
        numString += str(int(x)**2)
    # Return numString as an integer
    return int(numString)