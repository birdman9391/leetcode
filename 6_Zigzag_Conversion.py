class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        numPeriod = 2 * (numRows - 1)
        sLen = len(s)
        ret = ""
        
        index = 0
        while index < sLen:
            ret += s[index]
            index += numPeriod
        
        for row in range(1, numRows - 1):
            index = 0
            while index < sLen:
                if index + row < sLen:
                    ret += s[index + row]
                if index + numPeriod - row < sLen:
                    ret += s[index+ numPeriod - row]
                index += numPeriod
        index = numRows - 1
        while index < sLen:
            ret += s[index]
            index += numPeriod
                
        return ret
        