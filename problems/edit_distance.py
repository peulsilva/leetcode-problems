# https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        d = {}

        def compute_distance(i,j):
            if i >= len(word1):
                return max(len(word2)- j, 0)

            if j >= len(word2):
                return max(len(word1)-i, 0)

            if (i,j) in d:
                return d[(i,j)]

            if word1[i] == word2[j]:
                return compute_distance(i+1, j+1)

            else:
                option1 = compute_distance(i+1, j) # remove one of the characters
                option2 = compute_distance(i, j+1) # remove one of the characters 
                option3 = compute_distance(i+1, j+1) # change one of the characters



                d[(i,j)] = 1 + min([option1, option2, option3])
                return d[(i,j)]

        
        return compute_distance(0,0)
            