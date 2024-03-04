# https://leetcode.com/problems/coin-change/

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = [-1 for i in range(amount+1)]

        memo[0] = 0
        for x in range(amount+1):
            for coin in coins:
                if coin > amount:
                    continue

                if memo[x-coin] == -1:
                    continue

                if memo[x] == -1:
                    memo[x] = 1 + memo[x - coin]

                else:
                    memo[x] = min(memo[x], 1 + memo[x-coin])

        return memo[amount ]