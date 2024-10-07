# https://leetcode.com/problems/combination-sum-iv/

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def solve(i,curr):
            if curr > target : 
                return 0

            if curr == target:
                return 1

            if (i, curr) in dp:
                return dp[(i,curr)]
            ans = 0
            
            for num in nums:
                ans += solve(i+1, curr + num)

            dp[(i, curr)] = ans

            return ans


        return solve(0, 0)