# https://leetcode.com/problems/maximum-subarray
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def is_all_negative(nums):
            for el in nums:
                if el >=0:
                    return False
            
            return True

        if is_all_negative(nums):
            return max(nums)
        # f_m : largest subarray sum of a[0:m] containing a[m-1]
        # s_m : largest subarray of a[0:m] that can contain or not a[m-1]
        f_m, s_m = 0,0

        for i in range(len(nums)):
            f_m = nums[i] + max(f_m, 0)
            s_m = max(s_m, f_m)

        
        return s_m
        