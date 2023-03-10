# https://leetcode.com/problems/isomorphic-strings/

# Solution
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ruleMapping = dict()

        reverseMapping = dict()

        mappedStr = ""
        for i in range(0,len(s)):
            if s[i] not in ruleMapping and t[i] not in reverseMapping:
                ruleMapping[s[i]] = t[i]
                reverseMapping[t[i]] = s[i]
            try:
                mappedStr += ruleMapping[s[i]]
            except:
                pass


        if mappedStr == t:
            return True
        else:
            return False