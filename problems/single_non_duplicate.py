# https://leetcode.com/problems/single-element-in-a-sorted-array/
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        l, r = 0, n - 1
        mid = None

        while l < r:
            if r - l == 1:
                if l == 0:
                    if nums[l] != nums[r]:
                        return nums[l]

                elif r == n-1:
                    if nums[l] != nums[r]:
                        return nums[r]

                else:
                    if nums[l] == nums[l-1] or nums[l] == nums[l+1]:
                        return nums[r]
                    return nums[l]


            mid = (l+r)//2
            
            if nums[mid] == nums[mid+1] :
                if (n-mid)% 2 == 1:
                    l = mid

                else:
                    r = mid
            elif nums[mid] == nums[mid-1]:
                if (n-mid)% 2 == 1:
                    r = mid

                else:
                    l = mid
            else:
                return nums[mid]

        return nums[mid]               
