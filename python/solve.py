# Description:
# In this Kata, you will remove the left-most duplicates from a list of integers and return the result.
# Remove the 3's at indices 0 and 3
# followed by removing a 4 at index 1
# Examples:
# solve([3,4,4,3,6,3]) -> [4,6,3]
# solve([1,2,1,2,1,2,3]) -> [1,2,3]

def solve(arr):
    # Create empty list to hold counters to know which objects to remove from the arr list
    tempArr = []

    # Create two counter variables used in the below for loops
    countX = 0
    countY = 0

    # For loop to iterate through the arr list
    for x in arr:
        # Another for loop to again iterate through the arr list to allow us to compare objects within the same list
        for y in arr:
            # If conditional checking if countY is greater than countX and if the objects are the same. This is the only
            # time we want to chose a countX to remove when removing objects from the arr list
            if countX < countY and x == y:
                # Utilize the append function to add the countX counter to the temporary list to know which objects to
                # remove from arr later
                tempArr.append(countX)
                # Break from this iteration of the for loop because once we've hit the true statement, there's no reason
                # to check for anymore objects
                break
            # Increment the countY counter each time we iterate through the second for loop
            countY += 1
        # Increment the countX counter each time we iterate through the first for loop
        countX += 1
        # Set the countY counter each time we finish iterating through the second for loop to reset the counter back to
        # the beginning to match up with the secondary for loop
        countY = 0

    # Use the reverse function to reverse the tempArr list in order to easily pop the objects from the arr list
    tempArr.reverse()

    # For loop to iterate through the tempArr list
    for x in tempArr:
        # Pop (remove) each object from the arr list via the corresponding object in tempArr
        arr.pop(x)
    # Finally, return arr
    return arr