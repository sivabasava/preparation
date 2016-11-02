import sys
def get_profit(prices):
    buy = sys.maxint
    sell = 0
    for price in prices:
        buy = min(buy, price)
        sell = max(sell, price-buy)
    print prices, ' Profit: ',sell

get_profit([1,5,2,10])
get_profit([5,2,10])
get_profit([1,2,3,5])
