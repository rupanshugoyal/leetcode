# https://leetcode.com/problems/is-subsequence/

# Solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        sIndex = 0
        for i in range(0, len(t)):
            if s[sIndex] == t[i]:
                sIndex+=1
            if sIndex == len(s):
                return True
            
        return False