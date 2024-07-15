from collections import deque
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        q = deque()
        ans = [0 for _ in range(len(temperatures))]
        # q contains only lower temperatures 
        for i,temp in enumerate(temperatures):
            while True:
                if (len(q) == 0):
                    q.appendleft([temp,i])
                    break

                el = q.popleft()
                if el[0] < temp:
                    j = el[1]
                    ans[j] = i-j
                
                else:
                    q.appendleft(el)
                    q.appendleft([temp,i])
                    break
        return ans

        