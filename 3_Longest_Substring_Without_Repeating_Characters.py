class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndex = {}
        maxLen = 0
        startIndex = 0
        for i, c in enumerate(s):
            if c in lastIndex.keys() and lastIndex[c] >= startIndex:
                startIndex = lastIndex[c] + 1
            lastIndex[c] = i
            maxLen = max(i - startIndex + 1, maxLen)
            
        return maxLen