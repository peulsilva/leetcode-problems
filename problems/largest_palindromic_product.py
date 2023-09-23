# https://leetcode.com/problems/largest-palindrome-product/solutions/3281253/479-solution-with-step-by-step-explanation/
class Solution(object):
    @staticmethod
    def is_palindromic(s):
        return s == s[::-1]

    def largestPalindrome(self, n):
            """
            :type n: int
            :rtype: int
            """
            max_digits = n**2 + 1
            min_digits = 2*n

            max_value = 10**(n**2 + 1)
            min_value = 10**min_digits

            if n == 1:
                return 9

            max_pal = 0 
            for i in range(10**n - 1, 10**(n-1), -2):
                if i * i < max_pal:
                    break
                    
                for j in range(10**n - 1, i-1, -2):
                    if i*j < max_pal :
                        continue
                    
                    if Solution.is_palindromic(str(i * j)):
                        max_pal = max(i * j, max_pal)

            # for value in range(max_value, min_value, -1):
            #     s = str(value)

            #     if Solution.is_palindromic(s):

            #         return value % 1337

            #     print(value)

            return max_pal % 1337