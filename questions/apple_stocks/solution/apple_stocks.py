# The idea is to keep track of the local min, local max, and the 
# max profit so far. Everytime I redefine a max I recalculate the
# profit and see if it is greater than the max profit so far.
# time complexity: O(n^2)
# space complexity: O(1)

def max_stock_profit(stock_prices):
    """Returns the best time to buy & sell for the greatest profit"""

    highest_profit = None
    best_buy_num = None
    best_sell_num = None

    for buy_i in range(len(stock_prices)):

        for sell_i in range(buy_i, len(stock_prices)):

            current_profit = stock_prices[sell_i] - stock_prices[buy_i]

            if current_profit > highest_profit:
                highest_profit = current_profit
                best_buy_num = stock_prices[buy_i]
                best_sell_num = stock_prices[sell_i]

    return (highest_profit, best_buy_num, best_sell_num)


stock_prices = [100, 200, 300, 700, 50, 20, 40, 600]
max_stock_profit(stock_prices)
