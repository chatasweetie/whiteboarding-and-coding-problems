
def cocktail_sort(array):
    """A variable of Bubble Sort, that bubbles the largest to the left and
    smallest to the right

        >>> lst = [5, 1, 4, 2, 8, 0, 2]
        >>> print cocktail_sort(lst)
        [0, 1, 2, 2, 4, 5, 8]

        >>> lst2 = [3,5,6,323,234,234,234,23,42,34,234,23,42]
        >>> print cocktail_sort(lst2)
        [3, 5, 6, 23, 23, 34, 42, 42, 234, 234, 234, 234, 323]
        
        >>> lst3 = [1,0]
        >>> print cocktail_sort(lst3)
        [0, 1]

        >>> lst4 = [0, 1, 2, 2, 4, 5, 8]
        >>> print cocktail_sort(lst4)
        [0, 1, 2, 2, 4, 5, 8]
    """

    #Setting the boundaries for iteration
    min_index = 0
    max_index = len(array) - 1

    swapped = True

    while swapped:
        # resets swapped to False to see if there is a swap
        swapped = False

        #iteration going left to right
        for i in range(min_index, max_index):
            if array[i] > array[i+1]:
                #swapping numbers
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True

        #change the upper bound since we bubbled up the largest
        #number to the right
        max_index -= 1

        #iteration going right to left
        for i in range(min_index+1, max_index)[::-1]:
            if array[i] < array[i-1]:
                #swapping numbers
                array[i], array[i-1] = array[i-1], array[i]
                swapped = True

        #change the lower bound since we bubbled down the smallest
        #number to the left
        min_index += 1

    return array


lst = [5, 1, 4, 2, 8, 0, 2]

sort = cocktail_sort(lst)

print "*"*80
print sort


#####################################################################
# Don't touch the code below!
# This allows the doctests to run

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
