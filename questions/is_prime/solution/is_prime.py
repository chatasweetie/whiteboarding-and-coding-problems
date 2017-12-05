
def is_prime(num_to_check):
    """Returns bool if num is prime num

        >>> print is_prime(5)
        True
        >>> print is_prime(283)
        True
        >>> print is_prime(382)
        False
        >>> print is_prime(1)
        False
        >>> print is_prime(-41)
        False
    """

    if num_to_check < 2:
        return False

    for num in range(2, num_to_check):
        if num_to_check % num == 0:
            return False

    return True

print is_prime(5)
print is_prime(6)
print is_prime(89)
print is_prime(88)


#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
