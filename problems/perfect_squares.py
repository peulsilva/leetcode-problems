# https://leetcode.com/problems/perfect-squares/
class Solution:

    def numSquares(self, n: int) -> int:
        self.memo = {}
        return self.count_squares(n)

    def count_squares(self, n):
        if n < 4:
            return n

        sqrt_n = n ** (1/2)
        if sqrt_n == int(sqrt_n):
            return 1

        min_count = 1e10
        for i in range(int(sqrt_n), 0, -1):
            if self.memo.get(n-i**2) is None: 
                count = self.count_squares(n - i**2)
                self.memo[n - i**2] = count

            else:
                count = self.memo[n-i**2]

            if count + 1 < min_count:
                min_count = count + 1

        return min_count
        