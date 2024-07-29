# https://leetcode.com/problems/super-ugly-number/
from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1]
        
        # indexes[p]: last index i where dp[i]*p <= dp[-1]
        indexes= {p : 0 for p in primes}

        for (i) in range(n-1):
            next = 1e10
            for p,j in indexes.items():
                next = min(next, p*dp[j])

            for p,j in indexes.items():
                indexes[p] += dp[j] * p <= next

            dp.append(next)

        return dp[-1]
