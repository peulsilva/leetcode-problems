# https://leetcode.com/problems/jump-game-ii/
from typing import List
class Solution:
    

    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)

        M = {}
        
        def min_jumps(i,j):
            if i >= j:
                return 0

            if nums[i] >= j-i:
                return 1


            if (i,j) in M:
                return M[(i,j)]

            if nums[i] == 0:
                return 1e8

            jumps = 1e8
            for k in range(1, nums[i]+1):
                jumps = min(jumps, 1+ min_jumps(i+k, j))

            M[(i,j)] = jumps
            return jumps
        
        return min_jumps(0,n-1)