def greatest_stock_profit(list_of_stocks):
    """
    Input: List of integers?
    Floating points? non-numerical?
    Follow timeline so order matters

    Output: Integer reprenting greatest profit

    >>> greatest_stock_profit([10, 7, 5, 8, 11, 9])
    6
    >>> greatest_stock_profit([5, 8, 3, 20, 12, 25])
    22

    Pseduocode:
    1. Initialize a variable max_profit
    2. Iterate through arrays 
    3. Check whether list_of_stocks[j] - list_of_stocks[i] > max_profit
    4. If the max_profit is larger, update that to be newest max profit
    5. Return max_profit
    """
    max_profit = 0
    for i in range(len(list_of_stocks)):
        for j in range(i+1, len(list_of_stocks)):
            if list_of_stocks[j] - list_of_stocks[i] > max_profit:
                max_profit = list_of_stocks[j] - list_of_stocks[i]
    return max_profit



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n** ALL TESTS PASSED. AWESOME WORK! **\n")


# Time Complexity - O(n^2)
# Space Complexity - O(1)