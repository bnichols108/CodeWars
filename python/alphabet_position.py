# Description:
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
# Examples:
# alphabet_position("The sunset sets at twelve o' clock.") -> "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
# alphabet_position("The narwhal bacons at midnight.") -> "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"

def alphabet_position(text):
    # Dictionary to hold key:value pairs between alphabet:number
    alpha_dict = {"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"10","k":"11","l":"12","m":"13","n":"14","o":"15","p":"16","q":"17","r":"18","s":"19","t":"20","u":"21","v":"22","w":"23","x":"24","y":"25","z":"26",}

    # Empty string variable to return
    ret = str()

    # For loop to iterate through string argument with lower built-in function
    for char in text.lower():
        # For loop to iterate through the dictionary checking for each alphabet character
        for key,value in alpha_dict.items():
            # If conditional to check if current key and value are equal
            if key == char:
                # If true, add the value from the current key pair in the alpha_dict dictionary
                ret += value + " "

    # Return the string but remove the last character in the string because it's an empty character
    return ret[:-1]

