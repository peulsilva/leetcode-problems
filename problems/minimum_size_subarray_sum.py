# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cumsum = 0
        l,r = 0,0
        ans = 1e8
        while r < len(nums):
            cumsum += nums[r]

            while cumsum >= target:

                ans = min(ans, r-l+1)
                cumsum -= nums[l]
                l = l+1
            
            r += 1

        if ans == 1e8:
            return 0

        return ans
                
        