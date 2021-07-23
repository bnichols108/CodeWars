# Description:
# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# It’s guaranteed that array contains at least 3 numbers.
# The tests contain some very huge arrays, so think about performance.
# Examples:
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

def find_uniq(arr):
    # Create integer variable to count between the list items
    listItem = 0

    # If conditional to compare first two items in the arr list
    if arr[listItem] == arr[listItem+1]:
        # If true, we know the first two numbers are duplicates, so we can set a variable to remember the duplicate
        duplicate_num = arr[listItem]
    else:
        # If false, the duplicate number has to be the third item in the list, since this list will always have at least
        # three items
        duplicate_num = arr[listItem+2]

    # To make this script run faster, remove duplicates in the list
    arr = list(dict.fromkeys(arr))

    # If conditional checking for the non-duplicate number
    if arr[0] != duplicate_num:
        # If true, the first item in the arr list is the non-duplicate, so return that item
        return arr[0]
    else:
        # If false, the second item in the arr list is the non-duplicate, so return that item
        return arr[1]