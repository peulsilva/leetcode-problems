# https://leetcode.com/problems/container-with-most-water/
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        max_area = -1
        while l<r:
            this_area = (r-l) * min(height[l], height[r])
            if this_area > max_area:
                max_area = this_area
                
            if height[l] < height[r]:
                l+=1
            else:
                r -= 1
        return max_area