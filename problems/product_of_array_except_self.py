# https://leetcode.com/problems/product-of-array-except-self
from collections import deque
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        postfix = deque()
        result = []
        n = len(nums)

        for idx in range(n):
            el = nums[idx]
            if len(prefix) == 0:
                prefix.append(el)
                continue
            
            prefix.append(prefix[-1] * el)

        for reverse_idx in range(n-1,-1, -1):
            el = nums[reverse_idx]
            if len(postfix) == 0:
                postfix.append(el)
                continue
            postfix.appendleft(postfix[0] * el)

        result.append(postfix[1])

        for idx in range(1,n-1):
            a = prefix[idx-1]
            b = postfix[idx +1]

            result.append(a*b)
        
        result.append(prefix[-2])
        return result
