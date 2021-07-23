# Description:
# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the
# sake of simplicity, are named with letters from a to m.
# The colors used by the printer are recorded in a control string. For example a "good" control string would be
# aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one
# time color a...
# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g.
# aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
# You have to write a function printer_error which given a string will return the error rate of the printer as a string
# representing a rational whose numerator is the number of errors and the denominator the length of the control string.
# Don't reduce this fraction to a simpler expression.
# The string has a length greater or equal to one and contains only letters from ato z.
# Examples:
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"
# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"

import string

def printer_error(s):
    # Create integer variable to keep count of errors
    errors = 0

    # For loop to iterate through string s
    for x in s:
        # If conditional to see if char x is not in alphabet from a-m
        if x not in string.ascii_lowercase[:13]:
            # Since x is not between alphabet a-m, increase errors integer by one
            errors += 1

    # Return string to show errors over number of characters in s
    return (str(errors) + "/" + str(len(s)))