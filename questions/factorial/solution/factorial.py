
def factorial(num):
    """Returns the factorial of n
    n!

        >>> print factorial(4)
        24

        >>> print factorial(10)
        3628800

        >>> print factorial(1)
        1

        >>> print factorial(3)
        6
    """

    if num == 1:
        return 1

    total = num * factorial(num - 1)

    return total


print factorial(4)

#####################################################################
# Don't touch the code below!
# This allows the doctests to run

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
