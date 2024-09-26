# https://leetcode.com/problems/word-break

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def split_strings(curr):
            if curr in dp:
                return dp[curr]

            if curr == '':
                return True

            for word in wordDict:
                
                if curr.startswith(word):
                    if split_strings(curr[len(word):]):
                        dp[curr] = True
                        return True

            dp[curr] = False
            return False
            
        return split_strings(s)