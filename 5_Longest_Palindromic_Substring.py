import re

class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        pTable = [[0 for _ in range(sLen)] for __ in range(sLen)]
        for i in range(sLen):
            pTable[i][i] = 1
            maxString = s[i:i+1]
        for i in range(sLen - 1):
            if s[i] == s[i + 1]:
                pTable[i][i+1] = 1
                maxString = s[i:i+2]
        flag = [True, True]
        for l in range(2, sLen):
            flag.append(False)
            if flag[-3] == False:
                continue
            for i in range(sLen - l):
                j = i + l
                if s[i] == s[j] and pTable[i+1][j-1]>0:
                    pTable[i][j] = pTable[i+1][j-1] + 1
                    maxString = s[i:j+1]
                    flag[-1] = True
            if flag[-1] == False and flag[-2] == False:
                break
        return maxString