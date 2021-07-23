def duplicate_encode(word):
    # Empty string to return
    ret = ""
    # Modify word to be all same case to allow for case insensitive comparisons
    word = word.lower()

    # For loop to iterate through each character in word
    for char in word:
        # If conditional to determine the count of char in word
        if word.count(char) > 1:
            # If char found more than once in word, concatenate ")" to ret
            ret += ")"
        else:
            # If char found only once in word, concatenate "(" to ret
            ret += "("

    return ret