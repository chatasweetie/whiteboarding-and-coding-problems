def unique_char(string):
    """
    >>> unique_char("apple")
    'ale'
    >>> unique_char("banana")
    'b'
    >>> unique_char("aassccd")
    'd'

    Are the characters case sensitive?
    Are the characters special characters?
    Are the characters whitespace?
    Are the characters alphanumeric?

    Add a check to see if the string is empty.
    If empty, return an empty string.
    Create dictionary to store the characters and their counts
    Iterate through the string and add the characters to the dictionary.
    If the character is already in the dictionary, increment the count.
    If the character is not in the dictionary, add it to the dictionary with a count of 1.
    After creating the dictionary, iterate through the dictionary and return the character with a count of 1.
    If there is no character with a count of 1, return an empty string.

    Assume the characters are alphanumeric and same case.
    """
    if not string:
        return ""
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1
    # print(char_count)
    unique_char = ""
    for char, count in char_count.items():
        if count == 1:
            unique_char = unique_char + char
    return unique_char
print("\nunique_char tests:")
print(unique_char("APple"))
print(unique_char("banana"))
print(unique_char("aassccd"))
print(unique_char("11223456"))

# Space Complexity: O(n) - because we are using a dictionary to store the characters and their counts
# Time Complexity: O(n) - because we are iterating through the string once to create the dictionary and once to iterate through the dictionary


def unique_char_no_ds(string):
    """
    >>> unique_char_no_ds("apple")
    'ale'
    >>> unique_char_no_ds("banana")
    'b'
    >>> unique_char_no_ds("aassccd")
    'd'

    Add a check to see if the string is empty.
    If empty, return an empty string.
    Create a unique_char string.
    Iterate through the string and check if the character appears anywhere else in the string.
    If the character appears only once (at the current position), add it to the unique_char string.
    If no character is found, return an empty string.
    Return the unique_char string.

    Assume the characters are alphanumeric and same case.
    """
    if not string:
        return ""
    unique_char = ""
    for i in range(len(string)):
        # Check if this character appears anywhere else in the string
        is_unique = True
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                is_unique = False
                break
        if is_unique:
            unique_char = unique_char + string[i]
    return unique_char

print("\nunique_char_no_ds tests:")
print(unique_char_no_ds("apple"))
print(unique_char_no_ds("banana"))  
print(unique_char_no_ds("aassccd"))
print(unique_char_no_ds("11223456"))

# Time Complexity: O(n^2) - because we are iterating through the string twice
# Space Complexity: O(1) - because we are not using any additional data structures


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("ALL TESTS PASSED")