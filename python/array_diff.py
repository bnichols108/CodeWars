#Description:
#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#It should remove all values from list a, which are present in list b keeping their order.
#array_diff([1,2],[1]) == [2]
#If a value is present in b, all of its occurrences must be removed from the other:
#array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    # Variable to keep count of iterations through the second list
    listLocation = 0

    # List to hold the listLocation variable when true to then remove list a items
    listC = []

    # For loop to iterate through each item in list b
    for num1 in b:
        # listLocation needs to be set to 0 each time prior to looping through list a again
        listLocation = 0

        # For loop to iterate through each item in list a
        for num2 in a:
            # If conditional to compare list b item and list a item
            if num1 == num2:
                # If true, add current listLocation variable to listC list
                listC.append(listLocation)
            # Outside of the if conditional but within the for loop for list a, increment listLocation
            listLocation += 1
    # Remove duplicates from listC to not cause out of range errors
    listC = list(dict.fromkeys(listC))
    # Sort listC in reverse order to allow removal of items in list a
    listC.sort(reverse=True)

    # For loop to iterate through the listC items
    for num3 in listC:
        # Pop/remove the current item from list a
        a.pop(num3)

    # Return list a
    return a;