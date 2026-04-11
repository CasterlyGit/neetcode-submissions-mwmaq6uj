class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = prices[0]
        maxProfit = 0

        for i in prices[1:]:
            
            if maxProfit < i - minimum:
                maxProfit = i - minimum
            
            if i < minimum:
                minimum = i

        return maxProfit