# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        def solve(remaining_dices, cumsum):
            if (remaining_dices, cumsum) in dp:
                return dp[(remaining_dices,cumsum)]
            
            if remaining_dices == 0:
                return int(cumsum == target)

            if cumsum > target:
                return 0

            ans = 0
            for i in range(1,k+1):
                ans += solve(remaining_dices - 1, cumsum + i)

            dp[(remaining_dices, cumsum)] = ans % (1e9+7)
            return ans % (1e9+7)

        return int(solve(n, 0))