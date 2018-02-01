
def unique_char(message):
    """Returns all unique characters
    Time: O(n)
    Space O(n)

        >>> print unique_char("apple")
        ael
        >>> print unique_char("a")
        a
        >>> print unique_char("aa")
        <BLANKLINE>
    """
    unique_char_dict = {}

    for char in message:
        unique_char_dict[char] = unique_char_dict.get(char, 0) + 1

    unique_char_ls = []

    for char in unique_char_dict:
        if unique_char_dict[char] == 1:
            unique_char_ls.append(char)

    return "".join(unique_char_ls)

print unique_char("apple")
print unique_char("banana")


def unique_char_no_ds(message):
    """Returns all unique characters
    Time: O(n^2)
    Space O(n)

        >>> unique_char_no_ds("banana")
        'b'
        >>> unique_char_no_ds("b")
        'b'
        >>> unique_char_no_ds("bb")
        ''
    """
    unique_char = ""

    for i in range(len(message)):
        not_seen = True
        for j in range(len(message)):
            if i == j:
                continue
            if message[i] == message[j]:
                not_seen = False
                break
        if not_seen:
            unique_char = unique_char + message[i]

    return unique_char

print unique_char_no_ds("apple")
print unique_char_no_ds("banana")


#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
