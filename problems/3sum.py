# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        n = len(nums)
        
        for (idx, a) in enumerate(nums):
            if idx > 0 and a == nums[idx- 1]:
                continue

            l, r = idx + 1, n -1

            while l < r :
                

                if nums[r] + nums[l] + a == 0:
                    ans.append([a, nums[l], nums[r]])

                    l+= 1

                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                        
                    continue

                if nums[r] + nums[l] + a > 0:
                    r -= 1
                    continue

                if nums[r] + nums[l] + a < 0:
                    l += 1
                
                    
        return ans
                    