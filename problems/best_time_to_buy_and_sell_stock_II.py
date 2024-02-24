# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List
class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0

        for i in range(1,n):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]
        

        return profit
