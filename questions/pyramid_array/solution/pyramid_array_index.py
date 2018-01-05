
def present_in_pyramid(array, value):
    """ Returns Bool if value is in array

        >>> p_array = [ 1, 3, 4, 5, 7, 9, 7, 5, 5, 3, 0, -10]
        >>> present_in_pyramid(p_array, 0)
        False

        >>> p_array = [ 1, 3, 4, 5, 7, 9, 7, 5, 5, 3, 0, -10]
        >>> present_in_pyramid(p_array, 3)
        True
    """

    sm_left = array[0]
    sm_right = array[-1]
    mid = array[len(array)/2]

    if value < mid:
        a = array[:len(array)/2]
        b = array[len(array)/2:]
        if value > sm_left:
            if linear_binary_search(a, value):
                return True
        if value > sm_right:
            if linear_binary_search(b, value):
                return True

    return False


def linear_binary_search(array, value):
    """ Returns bool is value is in array using linear binary search

        >>> p = [1, 3, 4, 5, 7, 9]
        >>> print linear_binary_search(p, 8)
        False

        >>> p = [1, 3, 4, 5, 7, 9]
        >>> print linear_binary_search(p, 3)
        True
    """
    if len(array) == 1:
        if array[0] == value:
            return True
        else:
            return False

    if not array:
        return False

    mid_index = (len(array)/2)
    mid_value = array[mid_index]

    if mid_value == value:
        return True

    if value < mid_value:
        return linear_binary_search(array[:mid_index], value)

    if value > mid_value:
        return linear_binary_search(array[mid_index:], value)

p_array = [ 1, 3, 4, 5, 7, 9, 7, 5, 5, 3, 0, -10]
v = 0

print present_in_pyramid(p_array, 3)

#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
