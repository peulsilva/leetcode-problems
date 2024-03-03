# https://leetcode.com/problems/valid-parentheses/
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '{' : '}',
            '[' : ']',
            '(' : ')'
        }

        if len(s) % 2 != 0:
            return False

        queue = deque()

        for c in s:
            if c in pairs.keys():
                queue.appendleft(c)

            else:
                if len(queue) == 0:
                    return False

                a = queue.popleft()

                if pairs[a] != c:
                    return False
        
        if len(queue) > 0:
            return False
            
        return True
