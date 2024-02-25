# https://leetcode.com/problems/non-overlapping-intervals/
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        ans = 0

        sorted_by_start = sorted(intervals, key = lambda x: x[0])
        last_end = sorted_by_start[0][1]
        
        for i, (start, end) in enumerate(sorted_by_start):
            if i == 0:
                continue

            is_overlapping = start < last_end

            if is_overlapping:
                # erase the interval with larger end

                last_end = min(last_end, end)
                ans += 1

            else:
                last_end = end
                
        return ans