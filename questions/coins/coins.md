Coins
=====
Given an infinite supply of dimes and pennies, find the different amounts of
money that can be created with exactly `num_coins` coins.

For example, when num_coins = 3, you can create:
    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime

For example:
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

###Solutions

- [Jessica's Solution - Python2.7](https://github.com/chatasweetie/whiteboarding-and-coding-problems/blob/master/questions/coins/solution/coins.py)
- [Arcy's Solution - Python 3.12](./solution/coins_arcy.py)