# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        n = len(s)

        l, r = 0, 1

        letters = set([s[l]])
        ans = 1

        while True:
            ans = max(len(letters), ans)
            if r == n:
                break
            

            if s[r] not in letters:
                letters.add(s[r])
                r+= 1
                continue

            while s[r] in letters:
                letters.remove(s[l])
                l+=1

        return ans
        