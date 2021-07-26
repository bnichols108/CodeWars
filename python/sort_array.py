def sort_array(source_array):
    # Return a sorted array.

    for numOdd1 in source_array:
        if (numOdd1 % 2) == 0:
            break
        for numOdd2 in source_array:
            if (numOdd1 == numOdd2) or ((numOdd1 % 2) == 0):
                break
            else:
                print("It is odd")



sort_array([5, 3, 2, 8, 1, 4])