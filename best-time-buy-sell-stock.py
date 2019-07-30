# Given a list of integer, every element represents the stock price for each
# day. Return the maximum profit where you can perform one buy and one sell
# ex. [7, 1, 5, 3, 6, 4] would return 5 as you buy on the second day and sell
# on the fifth day


def maxProfit(prices):
    minPrice = float('inf')  # Initialize upperbound
    profit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price  # Find the minimum price
        elif price - minPrice > profit:
            profit = price - minPrice  # Find the current max profit

    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
