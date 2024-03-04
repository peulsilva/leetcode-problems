# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memo[i,j] is the longest common subsequence of text1[0 ... i] and text2[0 ... j]

        m,n = len(text1), len(text2)

        memo = [[0 for i in range(n)] for i in range(m)]

        # filling the first row

        memo[0][0] = int(text1[0] == text2[0])

        for j in range(1,n):
            if text1[0] == text2[j]:
                memo[0][j] =1
            
            else:
                memo[0][j] = memo[0][j-1]

        for i in range(1, m):
            if text1[i] == text2[0]:
                memo[i][0] = 1

            else:
                memo[i][0] = memo[i-1][0]

        # filling the remaining rows via recursion

        for i in range(1,m):
            for j in range(1,n):

                if text1[i] != text2[j]:
                    memo[i][j] = max(memo[i][j-1], memo[i-1][j])

                else:
                    memo[i][j] = memo[i-1][j-1] + 1

        return memo[m-1][n-1]
