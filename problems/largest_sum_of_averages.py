# https://leetcode.com/problems/largest-sum-of-averages/
from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)

        def partial_sum(i):
            s = 0
            for j in range(i,n):
                s+= nums[j]

            return s

        dp = {}

        def solve(i, n_avgs):
            if n - i <= n_avgs:
                return partial_sum(i)

            if n_avgs <= 0:
                return -1e9

            if (i, n_avgs) in dp:
                return dp[(i, n_avgs)]

            curr_sum = 0
            ans = 0
            for j in range(i, n):
                curr_sum += nums[j]
                ans = max(ans, 1/(j-i+1) *curr_sum + solve(j+1, n_avgs-1))

            dp[(i, n_avgs)] = ans

            return ans

        
        ans = solve(0, k)
        return ans

