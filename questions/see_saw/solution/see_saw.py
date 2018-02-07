
def is_see_saw(array):
    """Returns bool if the array has sum of all the numbers to
    the left of this number is equal to the sum of all the
    numbers to the right of it

    time: O(n)
    space: O(1)

        >>> is_see_saw([1, 10, 2, 5, 6, 9, 4, 1, 4, 8, 14, 6])
        True

        >>> is_see_saw([])
        False

        >>> is_see_saw([100])
        True

        >>> is_see_saw([100, 100])
        False

        >>> is_see_saw([100, 100, 100])
        True

    """

    total_value = 0

    for num in array:
        total_value = total_value + num

    left = 0
    right = total_value

    for num in array:
        right = right - num

        if right == left:
            return True

        left = left + num

    return False

values = [1, 10, 2, 5, 6, 9, 4, 1, 4, 8, 14, 6]
print is_see_saw(values)

#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
