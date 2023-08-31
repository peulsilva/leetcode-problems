# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        # edge cases

        if len(s) < 2 : 
            return -1
        
        if len(s) == 2:
            if s [0] == s[1]:
                return 0
            
            else:
                return -1

        first_appeared_at = {}
        n = -1
        low, high = 0, len(s) -1


        for i, digit in enumerate(s):
            j = first_appeared_at.get(digit)
            if (j is None):
                first_appeared_at[digit] = i
            
            else :
                n = max(n, i - j - 1 )

        
        return n 
