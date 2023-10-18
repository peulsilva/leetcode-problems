# https://leetcode.com/problems/kth-largest-element-in-a-stream
import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [num for num in nums]
        heapq.heapify(self.nums)

        

    def add(self, val: int) -> int:

        heapq.heappush(self.nums, val)
        while (len(self.nums) > self.k):
            last = heapq.heappop(self.nums)

        return self.nums[0]
        