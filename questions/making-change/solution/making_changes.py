
def make_change(amount, currency_values):
    """Returns the number of possiblities of making change

            >>> print make_change(4, [1, 2, 3])
            4

            >>> print make_change(4, [1, 2, 3, 4, 5])
            5

            >>> print make_change(2, [1, 2, 3, 4, 5])
            2

            >>> print make_change(20, [1, 2, 3, 4, 5])
            192
    """

    if amount == 0:
        return 1

    if not currency_values:
        return 0

    count = 0

    coin = currency_values.pop()

    num_possibilities = (amount / coin) + 1

    for i in range(num_possibilities):
        amount_left = amount - i * coin
        count += make_change(amount_left, currency_values[:])

    return count

print make_change(4, [1, 2, 3])


#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"

