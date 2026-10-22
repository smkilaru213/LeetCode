class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            currProfit = price - minPrice
            maxProfit = max(maxProfit, currProfit)
        return maxProfit