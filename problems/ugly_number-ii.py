# https://leetcode.com/problems/ugly-number-ii/
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        # n1 is the first index where n1*2 > dp[-1]
        # n2 is the first index where n2*3 > dp[-1]
        # n3 is the first index where n3*5 > dp[-1]
        n1, n2, n3 = 0,0,0

    
        for (i) in range(n-1):
            v1 = dp[n1]
            v2 = dp[n2]
            v3 = dp[n3]

            next = min(2*v1, 3*v2, 5*v3)

            n1 += v1*2 <= next
            n2 += v2*3 <= next
            n3 += v3*5 <= next

            dp.append(next)
        
        return dp[-1]