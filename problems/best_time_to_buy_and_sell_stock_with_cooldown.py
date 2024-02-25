# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1 :
            return 0

        self.memo = {}

        ans = self.profit(prices, 0, True,)
        print(self.memo)
        return ans

    def profit(self, prices, i, can_buy):
        if i > len(prices):
            return -1e6
        
        # case where we sold on day n-2 
        if i == len(prices):
            return 0
        
        if i == len(prices)-1:
            if can_buy:
                return 0

            # if we cannot buy, we must sell
            else:
                return prices[i]

        if (i, can_buy) in self.memo:
            return self.memo[(i, can_buy)]

        if can_buy:
            # buying today
            buy_profit = -prices[i] + self.profit(prices, i+1, False)
            
            # not buying today
            cooldown_profit = self.profit(prices, i+1, True)

            self.memo[(i, can_buy)] = max(buy_profit, cooldown_profit)

            return self.memo[(i, can_buy)]

        if not can_buy:
            # selling today
            sell_profit = prices[i] + self.profit(prices, i+2, True) 

            # not selling today
            cooldown_profit = self.profit(prices, i+1, False)

            self.memo[(i, can_buy)] = max(sell_profit, cooldown_profit)

            return self.memo[(i, can_buy)]