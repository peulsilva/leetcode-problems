# https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def solve(k):
            if k > n:
                return 0

            if k == n:
                return 1

            if n%k == 0:
                return max((n/k)**k, solve(k+1))

            r = n % k
            ans = 1
            for i in range(1,k+1):
                
                if i > k-r:
                    ans *= (n//k + 1)
                else:
                    ans *= n//k

            # print(ans, k, r)
            return max(ans, solve(k+1))
        
        return int(solve(2))