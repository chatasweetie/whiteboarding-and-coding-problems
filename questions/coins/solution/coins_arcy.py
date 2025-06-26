def coins(num_coins):
    """
    Given an infinite supply of dimes and pennies, find the different amounts of
    money that can be created with exactly `num_coins` coins.

    Input: Integer representing the number of coins
    Output: Set of integers representing the different amounts of money that can be created

    For example, when num_coins = 3, you can create:
    3 = penny + penny + penny
    12 = dime + penny + penny
    21 = dime + dime + penny
    30 = dime + dime + dime

    So only 10 and 1 cent coints available, sum up all different combinations of coins to get the total number of cents.
    >>> coins(0) == {0}
    True

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(11) == {65, 101, 38, 74, 11, 110, 47, 83, 20, 56, 92, 29}
    True

    Pseudocode: 
    1. Loop through all possible numbers of dimes (from 0 to num_coins)
    2. For each number of dimes, calculate how many pennies you have left
    3. Calculate the total value and add it to your set
    """
    coins = set()
    for num_dimes in range(num_coins + 1):
        num_pennies = num_coins - num_dimes
        total = num_dimes * 10 + num_pennies
        coins.add(total)
    return coins

def coins_recursive(num_coins):
    if num_coins == 0:
        return {0}
    
    results = set()
    # Try adding a penny to all previous results
    for prev_amount in coins_recursive(num_coins - 1):
        results.add(prev_amount + 1)
    # Try adding a dime to all previous results  
    for prev_amount in coins_recursive(num_coins - 1):
        results.add(prev_amount + 10)
    
    return results

def coins_dp(num_coins):
    # dp[i] = set of amounts possible with i coins
    dp = [set() for _ in range(num_coins + 1)]
    dp[0] = {0}
    
    for i in range(1, num_coins + 1):
        for prev_amount in dp[i-1]:
            dp[i].add(prev_amount + 1)  # add penny
            dp[i].add(prev_amount + 10) # add dime
    
    return dp[num_coins]

from itertools import combinations_with_replacement

def coins_itertools(num_coins):
    coin_values = [1, 10]  # penny, dime
    results = set()
    
    # Generate all possible combinations of coin types
    for combo in combinations_with_replacement(coin_values, num_coins):
        results.add(sum(combo))
    
    return results

def coins_bits(num_coins):
    results = set()
    # Each position can be penny (0) or dime (1)
    for i in range(2**num_coins):
        total = 0
        for j in range(num_coins):
            if (i >> j) & 1:  # if jth bit is 1
                total += 10   # dime
            else:
                total += 1    # penny
        results.add(total)
    return results

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n✨ ALL TESTS PASSED!\n")

# Time Complexity - O(n)
# Space Complexity - O(n)