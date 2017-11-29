import bstgenerator


def is_value_present(root, num):
    """Returns bool if the num is in the BST

        >>> my_bst = bstgenerator.make_BST(12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        >>> print is_value_present(my_bst, 99)
        False

        >>> print is_value_present(my_bst, 4)
        True
    """

    if root.data == num:
        return True

    if root.data > num:
        if root.left is None:
            return False
        return is_value_present(root.left, num)

    if root.data < num:
        if root.right is None:
            return False
        return is_value_present(root.right, num)


my_bst = bstgenerator.make_BST(12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print is_value_present(my_bst, 99)




#####################################################################
# Don't touch the code below!
# This allows the doctests to run

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
