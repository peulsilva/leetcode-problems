# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        num_ones = 0
        for el in nums:
            num_ones += el
        
        # we must find the contiguous sequence of size num_ones that 
        # contains the minimum num of zeros

        ans = 1e10
        count_zeros = 0
        for i, start in enumerate(range(-num_ones, n - num_ones)):

            if i == 0:
                for index in range(num_ones):

                    count_zeros += nums[start + index] == 0
            else:
                count_zeros += (nums[start + num_ones-1] == 0) - (nums[start - 1] ==0)

            ans = min(ans, count_zeros)

        return ans 