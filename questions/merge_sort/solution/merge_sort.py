
def merge_sort(array):
    """Returns a sorted list using Merge sort

        >>> merge_sort([45, 3, 646, 24, 78, 23, 58])
        [3, 23, 24, 45, 58, 78, 646]
    """

    if len(array) < 2:
        return array

    mid = int(len(array)/2)
    array1 = merge_sort(array[:mid])
    array2 = merge_sort(array[mid:])

    return merge(array1, array2)


def merge(array1, array2):
    """Merges lists"""

    result_list = []
    while len(array1) > 0 or len(array2) > 0:
        if not array1:
            result_list.extend(array2)
            array2 = []
        elif not array2:
            result_list.extend(array1)
            array1 = []
        elif array1[0] < array2[0]:
            result_list.append(array1.pop(0))
        else:
            result_list.append(array2.pop(0))

    return result_list

print merge_sort([2, 1, 7, 4])


#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
