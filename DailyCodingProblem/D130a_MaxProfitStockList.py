'''

The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in
those days. For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by
buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6. If the given array of prices is sorted in
decreasing order, then profit cannot be earned at all.

Follow up Problem similar to this:
https://www.geeksforgeeks.org/maximum-difference-between-two-elements/

'''

def maxProfitBuySell(prices):
    '''
    :param prices:
    :return:

    This approach is working by finding the local minima and local maxima in the list.
    Run time complexity is O(n)

    '''

    if len(prices) == 1: ## Cannot have a buy sell pair
        return

    lSize = len(prices)
    buySellPair = []

    i = 0
    while i<lSize-1:

        while i < (lSize-1) and prices[i] > prices[i+1]:
            ## Buying when cost is lesser than next day
            i+=1

        if i == lSize - 1:
            print("Prices are descending order - cannot make profit")
            break
        buy = i+1
        i+=1

        while i < lSize-1 and prices[i] < prices[i+1]:
            ## Selling when reaching highest profit, Keep as long as money increasing
            i+=1

        sell = i+1

        buySellPair.append((buy,sell))

    print(buySellPair)


maxProfitBuySell([100, 180, 260, 310, 40, 535, 695])

