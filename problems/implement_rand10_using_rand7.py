# https://leetcode.com/problems/implement-rand10-using-rand7/

def rand7():
    ...
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        d = {}
        
        this_value = 1
        count = 0
        for i in range(1,8):
            for j in range(1,8):
                if this_value > 10:
                    break
                d[(i,j)] = this_value
                count+=1
                if (count >= 4):
                    this_value += 1
                    count = 0

        def generate_recursive(): 
            x, y = rand7(), rand7()
            if (x,y) in d:
                return d[(x,y)]

            else:
                return generate_recursive()

        return generate_recursive()