# https://leetcode.com/problems/last-stone-weight
import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = [-s for s in stones]
        heapq.heapify(l)

        while (len(l) > 1):
            high1 = - heapq.heappop(l)
            high2 = - heapq.heappop(l)

            if (high1 == high2):
                continue 
            
            else :
                heapq.heappush(l, - (high1 - high2))

        if len(l)==0:
            return 0
        
        return -l[0]
        