from morsecodetree import morse_code_tree


def translate_morse_code(array):
    """Translates morse code

    Takes in an array of morse code, returns the string

        >>> print translate_morse_code(["....", ".."])
        hi

        >>> print translate_morse_code([".--.", "-.--", "-", "....", "---", "-."])
        python

    """
    decoded = ""
    for code in array:
        current = morse_code_tree.root
        for char in code:
            if char == ".":
                current = current.left
            if char == "-":
                current = current.right
        decoded = decoded + current.data

    return decoded


print translate_morse_code(["....", ".."]) #=> "hi"


#####################################################################
# Don't touch the code below!
# This allows the doctests to run

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
