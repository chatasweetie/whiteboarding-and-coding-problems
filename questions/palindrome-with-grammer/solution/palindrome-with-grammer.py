def palindrome(phrase):
    """"Takes a str return whether or not it forms a palindrome
    ignoring case and non-alphabetical characters

        >>> palindrome("level")
        True

        >>> palindrome('algorithm')
        False

        >>> palindrome('A man, a plan, a canal: Panama.')
        True

    """
    start = 0
    end = len(phrase) - 1
    grammer = {" ", ".", ":", ","}
    while (start <= end):
        if (phrase[start] in grammer):
            start+=1
            continue
        if (phrase[end] in grammer):
            end-=1
            continue
        if (phrase[start].lower() != phrase[end].lower()):
            return False
        start+=1
        end-=1
    return True


#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"