# https://leetcode.com/problems/longest-palindrome/

# Solution

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        occurancesCount={}
        
        for charc in s:
            if charc in occurancesCount:
                occurancesCount[charc] += 1
            else:
                occurancesCount[charc] = 1

        maxpalindromelength = 0
        OddChar = 0
        for key in occurancesCount:
            if occurancesCount[key] %2 == 0:
                maxpalindromelength += occurancesCount[key]
            else:
                maxpalindromelength += (occurancesCount[key]//2)*2
                OddChar = 1
        
        maxpalindromelength += OddChar
        return maxpalindromelength