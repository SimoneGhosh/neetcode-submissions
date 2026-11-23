class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        buy = prices[0]

        for sell in prices:
            if buy > sell:
                buy = sell
            
            out = max (sell-buy, out)
        
        return out