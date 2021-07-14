# In this kata, we will make a function to test whether a period is late.
# Our function will take three parameters:
# last - The Date object with the date of the last period
# today - The Date object with the date of the check
# cycleLength - Integer representing the length of the cycle in days
# Return true if the number of days passed from last to today is greater than cycleLength. Otherwise, return false.

def period_is_late(last,today,cycle_length):
    # Import datetime library
    from datetime import date
    
    # Create delta between dates
    delta = today - last
    
    # Conditional to check delta days against cycle_length days
    if delta.days > cycle_length:
        return True;
    else:
        return False;