from typing import List
# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        # memo[i]: maximum ammount that you can get from houses [i, ..., j]
        memo = {}

        def rob_recursive(i, j):
            if j == i:
                return nums[i]

            if j< i:
                return 0

            if j in memo:
                return memo[j]

            memo[j] = max(rob_recursive(i,j-1), rob_recursive(i,j-2)+nums[j])

            return memo[j]

        v1 = rob_recursive(0, n-2)
        memo = {}
        v2 = rob_recursive(1,n-1)

        return max(v1, v2)
