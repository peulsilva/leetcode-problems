from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        l, r = 0, n-1

        while l<r:
            mid =(l+r)//2 

            print(l,mid, r)
            if mid == l: 
                if nums[l] > nums[r]:
                    return l
                
                return r

            if mid == r:
                if nums[l] > nums[r]:
                    return l
                
                return r

            if nums[mid] > nums[mid + 1]:
                r = mid
                continue
                
            l = mid

        return l
