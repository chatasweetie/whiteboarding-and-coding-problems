
def remove_dups(word):
    """returns str without any duplicate letters
    time: O(n)
    space: O(n)

        >>> remove_dups("google")
        'gole'

        >>> remove_dups("hello world")
        'helo wrd'

        >>> remove_dups("Jane Smith")
        'Jane Smith'

    """

    dups = set([])

    no_dups_word = []

    for char in word:
        if char not in dups:
            no_dups_word.append(char)
            dups.add(char)

    return "".join(no_dups_word)


print remove_dups("google")

#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
