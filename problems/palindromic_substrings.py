# https://leetcode.com/problems/palindromic-substrings/

def countSubstrings(self, s: str) -> int:
    n = len(s)
    count = 0
    for i,char in enumerate(s):


        # odd palindromes
        l,r = i,i
        while (l >=0 and r< n):
            if s[l] == s[r]:
                count+=1
                l -=1
                r +=1
            else:
                break

        #even palindromes
        l, r = i, i +1
        while (l >=0 and r< n):
            if s[l] == s[r]:
                count+=1
                l -=1
                r +=1
            else:
                break

    
    return count
        