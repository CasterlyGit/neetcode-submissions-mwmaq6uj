class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices) - 1):        
            j = len(prices) - 1
            while i < j:
                if prices[j] > prices[i] and prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]
                j -=1
        return maxProfit