##########################################
#              Version 1                 #
##########################################

VOWLES = ("a", "e", "i", "o", "u")


def file_contents(filename):
    """Returns the file's data as a string"""

    with open(filename) as f:
        file_data = f.read()
    f.close()

    return file_data


def counts_vowels(word):
    """Returns total number of vowels in a word"""
    vowel_count = 0

    for char in word:
        if char.lower() in VOWLES:
            vowel_count += 1

    return vowel_count


def total_num_of_vowels_from_string(txt):
    """Returns total number of vowels that appear in a string"""

    txt = txt.split()

    vowel_num = 0

    for word in txt:
        vowel_num += counts_vowels(word)

    return vowel_num


def returns_total_num_of_vowels(filename):
    """Returns total number of vowels in a file"""

    raw_data = file_contents(filename)
    num_of_vowels = total_num_of_vowels_from_string(raw_data)

    return num_of_vowels

total_num_vowels = returns_total_num_of_vowels("greeneggs.txt")

##########################################
#              Version 2                 #
##########################################

def total_num_of_vowels_from_string_v2(txt):
    """Returns total number of vowels that appear in a string"""

    vowel_num = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    txt = txt.split()

    for word in txt:
        for char in word:
            if char.lower() in VOWLES:
                vowel_num[char.lower()] = vowel_num[char.lower()] + 1

    return vowel_num


def returns_total_num_of_vowels_v2(filename):
    """Returns total number of vowels in a file"""

    raw_data = file_contents(filename)
    num_of_vowels = total_num_of_vowels_from_string_v2(raw_data)

    return num_of_vowels

total_num_vowels_v2 = returns_total_num_of_vowels_v2("greeneggs.txt")
