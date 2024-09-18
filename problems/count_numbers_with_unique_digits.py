class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = {}
        dp[0] = 1
        dp[1] = 10
        cumsum = 1

        def fact(n):
            if n == 1:
                return 1
            return n* fact(n-1)

        for i in range(2,n+1):
            dp[i] = 9 * fact(9)/fact(10-i) + dp[i-1]
        
        return int(dp[n])