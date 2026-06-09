class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        buy = 0
        for sell in range(len(prices)):
            profit = prices[sell] - prices[buy]
            if profit < 0:
                buy = sell
            maximum = max(maximum, profit)
        return maximum
