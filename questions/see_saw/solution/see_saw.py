
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


def is_see_saw_v2(array):
    """Returns bool if the array has sum of all the numbers to
    the left of this number is equal to the sum of all the
    numbers to the right of it

    time: O(n)
    space: O(1)

        >>> is_see_saw_v2([1, 10, 2, 5, 6, 9, 4, 1, 4, 8, 14, 6])
        True

        >>> is_see_saw_v2([])
        False

        >>> is_see_saw_v2([100])
        True

        >>> is_see_saw_v2([100, 100])
        False

        >>> is_see_saw_v2([100, 100, 100])
        True

    """
    # All single len arrays are 'balanced'
    if len(array) == 1:
        return True
    # All len 2 arrays cannot be 'balanced'
    if len(array) == 2:
        return False

    middle_i = len(array)/2
    left_value = 0
    right_value = 0

    for i in range(len(array)):
        if i > middle_i:
            left_value = left_value + array[i]
        if i < middle_i:
            right_value = right_value + array[i]

    current = middle_i

    for i in range(len(array)/2):

        if left_value == right_value:
            return True

        if left_value > right_value:
            right_value = right_value + array[current]
            current = current - 1
            left_value = left_value - array[current]

        if left_value < right_value:
            left_value = left_value + array[current]
            current = current + 1
            right_value = right_value - array[current]

    return False


print is_see_saw_v2(values)

#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
