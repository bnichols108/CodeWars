# Description:
# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four
# nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical
# structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
# Create a function which translates a given DNA string into RNA.
# The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.
# Examples:
# "GCAT"  =>  "GCAU"

def dna_to_rna(dna):

    # If there is no T in the variable, no need to make any changes, so pass and exit.
    if "T" not in dna:
        pass

    # Create list from dna string
    dnaFix = list(dna)
    # Create counter variable
    count = 0

    # For loop to iterate through the created list
    for x in dnaFix:
        # If conditional checking for the T in the list
        if x == "T":
            # If true, replace the T with the letter U in the same object location in the list via the counter
            dnaFix[count] = "U"
        # Increment the counter after each if conditional check while in the for loop
        count += 1

    # Return the list by converting it to a string with the .join function
    return "".join(dnaFix)