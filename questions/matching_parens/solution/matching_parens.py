
def has_matching_parens_v1(s):
    """Returns bool only if () parenthese are matching in a string

        >>> str = "(I(really)love (al(g)or)ithms)"
        >>> has_matching_parens_v1(str)
        True

        >>> str2 = "(I(really))love (al(g)or)ithms)"
        >>> has_matching_parens_v1(str2)
        False
    """

    parenthese = 0

    for char in s:
        if char == "(":
            parenthese += 1
        if char == ")":
            parenthese -= 1
        if parenthese < 0:
            return False
    if parenthese:
        return False

    return True


def has_matching_parens_v2(s):
    """Returns bool only if (),[] & {} parenthese are matching in a string

        >>> str2 = "([])"
        >>> has_matching_parens_v2(str2)
        True

        >>> str2 = "([{]})"
        >>> has_matching_parens_v2(str2)
        False
    """

    stack = []
    openings = {"(", "[", "{"}
    pairs = {")": "(",
             "]": "[",
             "}": "{",
            }

    for char in s:
        if char in openings:
            stack.append(char)

        if char in pairs:
            if not stack:
                return False
            if pairs[char] != stack[-1]:
                return False
            stack.pop()

    if stack:
        return False

    return True





#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
