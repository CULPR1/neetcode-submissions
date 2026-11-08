class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        min_buy = 100
        max_profit = 0
        for i in range(size):
            if min_buy > prices[i]:
                min_buy = prices[i]
            else: 
                if max_profit < prices[i] - min_buy:
                    max_profit = prices[i] - min_buy


        return max_profit