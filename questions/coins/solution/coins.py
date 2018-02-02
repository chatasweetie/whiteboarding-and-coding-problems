
def coins(num):
    """Returns different amounts of money that can be created by num coins

        >>> coins(0)
        set([0])

        >>> coins(1)
        set([1, 10])

        >>> coins(2)
        set([2, 11, 20])

        >>> coins(3)
        set([3, 12, 21, 30])

        >>> coins(11)
        set([65, 101, 38, 74, 11, 110, 47, 83, 20, 56, 92, 29])
    """

    values = {num}
    current_value = num

    for x in range(num):
        current_value += 9
        values.add(current_value)

    return values

print coins(11)

#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
