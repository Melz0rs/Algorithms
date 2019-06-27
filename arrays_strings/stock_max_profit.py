import sys


def stock_max_profit(stocks):
    current_max_profit = 0
    current_min_stock = sys.maxsize

    for i in range(len(stocks)):
        current_stock = stocks[i]

        current_min_stock = min(current_min_stock, current_stock)

        current_max_profit = max(current_max_profit, current_stock - current_min_stock)

    return current_max_profit


stocks = [45, 24, 35, 31, 40, 38, 11]

max_profit = stock_max_profit(stocks)

print(f'max_profit: {max_profit}')
