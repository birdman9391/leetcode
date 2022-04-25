import string

class customDict(dict):
    def __lt__(self, other):
        for ch in string.ascii_lowercase:
            if self[ch] < other[ch]:
                return True
            elif self[ch] > other[ch]:
                return False
        return False

    def __le__(self, other):
        for ch in string.ascii_lowercase:
            if self[ch] < other[ch]:
                return True
            elif self[ch] > other[ch]:
                return False
        return Trie

    
    def __gt__(self, other):
        for ch in string.ascii_lowercase:
            if self[ch] > other[ch]:
                return True
            elif self[ch] < other[ch]:
                return False
        return False

    def __ge__(self, other):
        for ch in string.ascii_lowercase:
            if self[ch] > other[ch]:
                return True
            elif self[ch] < other[ch]:
                return False
        return True


def computeDict(str):
    charCount = customDict({ch:0 for ch in string.ascii_lowercase})
    for ch in str:
        charCount[ch] += 1
    return charCount

   

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        charCounts = [[ztr, computeDict(ztr)] for ztr in strs]
        
        sortedStrs = sorted(charCounts, key = lambda item: item[1])

        prev_ztr, prevDict = sortedStrs[0]
        answer = [[prev_ztr]]

        for ztr, charDict in sortedStrs[1:]:
            if prevDict == charDict:
                answer[-1].append(ztr)
            else:
                answer.append([ztr])
            prevDict = charDict
        return answer
            
        