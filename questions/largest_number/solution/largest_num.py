
def largest_num(lst):
    """Returns the largest number possible with a lst of nums

    time: O(n^2)
    space: O(1)

        >>> lst = [3, 30, 34, 5, 9, 31]
        >>> largest_num(lst)
        953433130

        >>> lst2 = [777, 23, 4009, 8]
        >>> largest_num(lst2)
        8777400923
    """

    str_lst = [str(x) for x in lst]

    swapped = True

    while swapped:
        swapped = False

        for i in range(len(str_lst) - 1):
            current = str_lst[i]
            next = str_lst[i + 1]
            if int(next + current) > int(current + next):
                str_lst[i] = next
                str_lst[i + 1] = current
                swapped = True

    return int("".join(str_lst))

lst = [3, 30, 34, 5, 9, 31]
largest_num(lst)




#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
