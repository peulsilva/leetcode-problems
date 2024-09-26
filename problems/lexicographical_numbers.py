# https://leetcode.com/problems/lexicographical-numbers/
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(curr:int, n):
            ans.append(curr)
            curr_s = str(curr)

            option1 = int(curr_s + '0') 
            option2 = curr + 1

            if option1 <= n:
                dfs(option1, n)
            
            if not curr_s.endswith('9') and option2 <= n:
                dfs(option2, n)

        dfs(1,n)
        return ans
            
