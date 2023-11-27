# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        return max(0, self.max_profit(prices, 0, n)[0])

    def maxProfitNaive(self,prices, l, r):
        max_profit = 0
        for i in range(l, r):
            for j in range (i, r):
                max_profit = max(prices[j] - prices[i], max_profit)
        
        return max_profit
    
    def min_naive(self, prices, l, r):
        m = prices[l]
        for i in range(l, r):
            m = min(m, prices[i])

        return m

    def max_naive(self, prices, l, r):
        m = prices[l]
        for i in range(l, r):
            m = max(m, prices[i])

        return m
                

    def max_profit(self, prices, l, r):
        if abs(l-r)<= 3:
            return self.maxProfitNaive(prices, l, r), \
                self.min_naive(prices,l,r ), \
                self.max_naive(prices, l, r)
        
        mid = (l+r)//2
        opt_left, min_left, max_left = self.max_profit(prices, l, mid)
        opt_right, min_right, max_right = self.max_profit(prices, mid, r)

        best = max(opt_left, opt_right)
        best = max(best, max_right - min_left)

        return best, min(min_left, min_right), max(max_left, max_right)
        