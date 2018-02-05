
def power_set(values):
    """Returns all the power sets of a list

        >>> print power_set(['a','b','c'])
        [[], ['c'], ['b'], ['b', 'c'], ['a'], ['a', 'c'], ['a', 'b'], ['a', 'b', 'c']]

        >>> power_set([1,2])
        [[], [2], [1], [1, 2]]

        >>> power_set([])
        [[]]
    """

    if not values:
        return [[]]

    remaining = power_set(values[1:])
    return remaining + [[values[0]] + x for x in remaining]


print power_set(['a', 'b', 'c'])


#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
