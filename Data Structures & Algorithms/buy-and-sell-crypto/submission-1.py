class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - minimum
            max_profit = max(max_profit, profit)
            minimum = min(minimum, prices[i])

        return max_profit
            


        
        