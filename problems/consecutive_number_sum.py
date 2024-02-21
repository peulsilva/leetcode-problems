# https://leetcode.com/problems/consecutive-numbers-sum/

class Solution:

    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        k = int((2*n)**0.5)
        
        for m in range(1,k+1):
            if (2*n)%m==0 and (2*n/m)%2 != m%2:
                count +=1
                
        return count