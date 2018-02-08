
def lonely_num(numbers):
    """Returns the single occurring number

    time: O(n)
    space: O(n)

        >>> lonely_num([2, 6, 3, 8, 6, 2, 3])
        8

        >>> lonely_num([1,2,2,2,3,4,4,3,3,1])
        False

        >>> lonely_num([1,2,2,2,3,4,4,3,3,])
        1
    """

    values = {}

    for num in numbers:
        values[num] = values.get(num, 0) + 1

    for num in values:
        if values[num] == 1:
            return num

    return False


nums = [2, 6, 3, 8, 6, 2, 3]
print lonely_num(nums)

#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
