class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sCount = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if s[sCount] == t[i]:
                if len(s) == sCount + 1:
                    return True
                sCount += 1 
