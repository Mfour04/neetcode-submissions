class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprices = float("inf")
        maxProfit = 0
        for price in prices:
            minprices = min(minprices, price)
            profit = price - minprices
            maxProfit = max(maxProfit, profit)
        return maxProfit




