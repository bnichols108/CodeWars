# Description:
# My friend wants a new band name for her band. She like bands that use the formula: "The" + a noun with the first
# letter capitalized, for example:
# "dolphin" -> "The Dolphin"
# However, when a noun STARTS and ENDS with the same letter, she likes to repeat the noun twice and connect them
# together with the first and last letter, combined into one word (WITHOUT "The" in front), like this:
# "alaska" -> "Alaskalaska"
# Complete the function that takes a noun as a string, and returns her preferred band name written as a string.
# Examples:
# band_name_generator("knife") -> "The Knife"
# band_name_generator("tart") -> "Tartart"

def band_name_generator(name):
    # If conditional to check if the name variable has the same character at the beginning and end of the string
    if name[0] == name[-1]:
        # Since true, return the name concatenated with name again but with the first character capitalized in the
        # string via the capitalize function
        return (name + name[1:]).capitalize()
    else:
        # Since false, return the name with "The" in the front while using the title function to capitalize each word
        return ("The " + name).title()