def palindrome(string):
    """"Takes a str and returns the longest palindrome

        >>> palindrome('add')
        'dad'

        >>> palindrome('ehhsieood')
        'oheseho'

    """

    char_count = {}

    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    palindrome = []

    for char in char_count:
        if char_count[char] % 2 != 0:
            single_char = char
        pair_num = char_count[char] / 2
        for num in range(pair_num):
            palindrome.insert(0, char)
            palindrome.append(char)

    if single_char:
        palindrome.insert((len(palindrome)/2), single_char)

    return "".join(palindrome)


#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
