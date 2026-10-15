class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        sell = prices[0]

        for i in range(1, len(prices)):
            p = prices[i]
            if p >= sell:
                maxProfit = max(maxProfit, p - sell)
            else:
                sell = p
            
        return maxProfit