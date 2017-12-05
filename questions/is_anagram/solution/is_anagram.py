
def are_anagrams(str1, str2):
    """Returns bool if two strings are anagrams

        >>> print are_anagrams("cat", "dog")
        False

        >>> print are_anagrams("banana", "dog")
        False

        >>> print are_anagrams("cat", "cat")
        True

    """
    dict1 = {}
    dict2 = {}

    # micor optimization: if the two strings are not
    # the same length, then fail fast
    if len(str1) == len(str2):

        for char in str1:
            dict1[char] = dict1.setdefault(char, 0) + 1

        for char in str2:
            dict2[char] = dict2.setdefault(char, 0) + 1

        for key in dict1:
            if dict1.get(key) != dict2.get(key):
                return False

        return True

    return False


print are_anagrams("cat", "dog")
print are_anagrams("cat", "cat")
print are_anagrams("cat", "cats")


#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
