# https://leetcode.com/problems/longest-palindromic-substring/editorial/
class Solution:
    def longest_palindrome_naive(self, s: str) -> str:
        """O(n^3 solution)

        Args:
            s (str): _description_

        Returns:
            str: _description_
        """        


        # edge cases
        if len(s) <= 1:
            return s

        if s == s[::-1]:
            return s

        low, high = 0, len(s)
        palindromes = [""]
        max_palindrome = ""

        for low in range(len(s)):
            for high in range(len(s) + 1):
                if low >= high:
                    continue

                sliced_s = s[low:high]

                if (sliced_s) == sliced_s[::-1]:
                    palindromes.append(sliced_s)
        
        
        for x in palindromes :
            if len(x) > len(max_palindrome):
                max_palindrome = x

        return max_palindrome
    
    
