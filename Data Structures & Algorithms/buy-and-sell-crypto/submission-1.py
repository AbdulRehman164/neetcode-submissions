class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyDay = 0
        for i in range(len(prices)):
            profit = max(prices[i] - prices[buyDay], profit)
            if prices[i] < prices[buyDay]:
                buyDay = i
        return profit
