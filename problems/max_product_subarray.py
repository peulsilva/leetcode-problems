# https://leetcode.com/problems/maximum-product-subarray/
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f_m, g_m, s_m = nums[0], nums[0], nums[0]

        for i in range(1,len(nums)):
            f_m_1 = max([nums[i], f_m*nums[i], g_m*nums[i]])
            g_m = min([nums[i], g_m*nums[i],f_m *nums[i]])
            f_m = f_m_1
            s_m = max([s_m, f_m])

        
        return s_m
        