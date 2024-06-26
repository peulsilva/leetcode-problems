# https://leetcode.com/problems/coin-change-ii/description/
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memo[x]: number of combinations of coins that make up to x
        
        # dfs[i, a] := number of combinations of coins that sums to 
        # a, given that we are using {coins[i], coins[i+1], ...}
        # dfs[i,0] = 0
        # dfs[i,a] = dfs[i, a - coins[i]] + dfs[i+1, a - coins[i+1]] + ...  
        dp = {}

        def dfs(i,a):
            if a == 0:
                return 1
            
            if a < 0 or i >= len(coins):
                return 0

            if (i,a) in dp:
                return dp[(i,a)]

            dp[(i,a)] = dfs(i, a - coins[i]) + dfs(i+1, a)
            return dp[(i,a)]

        return dfs(0,amount)
