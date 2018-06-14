class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if not prices: return max_profit

        buy_price = prices[0]

        for i in range(len(prices)):
            buy_price = min(buy_price, prices[i])
            max_profit = max(max_profit, prices[i]-buy_price)

        return max_profit