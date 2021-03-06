# Description:
# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the
# sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once
# (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and
# punctuation.
# Examples:
# is_pangram("pangram") -> False
# is_pangram("The quick brown fox jumps over the lazy dog") -> True

import string

def is_pangram(s):
    # For loop to iterate through each character in the alphabet
    for x in list(string.ascii_lowercase):
        # If conditional to check if each character in the alphabet is in the s string
        if x not in s.lower():
            # If the character is not in the s string, return False
            return False
    # At this point, if each character in the alphabet was found in the For loop, return True
    return True