class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0

        first_profits = [0]*len(prices)
        second_profits = [0]*len(prices)

        buy_price = prices[0]

        for i in range(1, len(prices)):
            buy_price = min(buy_price, prices[i])
            first_profits[i] = max(first_profits[i-1], prices[i]-buy_price)

        sell_price = prices[-1]

        for i in range(len(prices)-2, -1, -1):
            sell_price = max(sell_price, prices[i])
            second_profits[i] = max(second_profits[i+1], sell_price-prices[i])

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, first_profits[i]+second_profits[i])

        return max_profit