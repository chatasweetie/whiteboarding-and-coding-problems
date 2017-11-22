# You have a bunch of jars labeled 1 to N.
# You are given a set of instructions detailing how much
# candy to put in each jar. After you finish all the
# instructions, you need to return the average number of
# candies in each jar.


def average_amount_jar(candy_instructions):
    """Returns the average amount of candies for jars

        >>> candy_instructions = [5, [1, 2, 100], [2, 5, 100], [3, 4, 100]]
        >>> print average_amount_jar(candy_instructions)
        160

        >>> candy_instructions2 = [7, [1, 2, 200], [4, 6, 10], [1, 7, 25], [6, 7, 100]]
        >>> print average_amount_jar(candy_instructions2)
        115

        >>> candy_instructions3 = [7, [1, 2, 200]]
        >>> print average_amount_jar(candy_instructions3)
        57

        >>> candy_instructions4 = [2, [1, 2, 200]]
        >>> print average_amount_jar(candy_instructions4)
        200
    """

    # create jars
    jars = []
    for num in range(candy_instructions[0]):
        jars.append(0)

    #distribute candies
    for values in candy_instructions[1:]:
        start_jar = values[0] - 1
        end_jar = values[1]
        amount = values[2]
        for jar_num in range(start_jar, end_jar):
            jars[jar_num] += amount

    #add all the candy
    total_sum = 0
    for num in jars:
        total_sum += num

    #return avg
    return total_sum/candy_instructions[0]


def average_amount_jar_2(candy_instructions):
    """Returns the average amount of candies for jars

        >>> candy_instructions = [5, [1, 2, 100], [2, 5, 100], [3, 4, 100]]
        >>> print average_amount_jar_2(candy_instructions)
        160

        >>> candy_instructions2 = [7, [1, 2, 200], [4, 6, 10], [1, 7, 25], [6, 7, 100]]
        >>> print average_amount_jar_2(candy_instructions2)
        115

        >>> candy_instructions3 = [7, [1, 2, 200]]
        >>> print average_amount_jar_2(candy_instructions3)
        57

        >>> candy_instructions4 = [2, [1, 2, 200]]
        >>> print average_amount_jar_2(candy_instructions4)
        200
    """

    total_candy = 0

    #add all the candy
    for values in candy_instructions[1:]:
        start_jar = values[0] - 1
        end_jar = values[1]
        amount = values[2]
        for jar_num in range(start_jar, end_jar):
            total_candy += amount

    #return avg
    return total_candy/candy_instructions[0]


candy_instructions = [5, [1, 2, 100], [2, 5, 100], [3, 4, 100]]

print average_amount_jar(candy_instructions)
avg_amount_2 = average_amount_jar_2(candy_instructions)

#####################################################################
# Don't touch the code below!
# This allows the doctests to run

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
