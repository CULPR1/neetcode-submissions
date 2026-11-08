class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        max_price = 0
        for i in range(size -1):
            for j in range(i + 1,size):
                if prices[i] >= prices[j]:
                    continue
                else:
                    profit = prices[j] - prices[i]
                    if max_price < profit:
                        max_price = profit

        return max_price