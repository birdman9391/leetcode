class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        ans = []
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        
        # nums.sort()
        keys = list(dic.keys())
        keys.sort()
        nLen = len(keys)

        for i in range(nLen):
            for j in range(i, nLen):
                if i == j and dic[keys[i]] < 2:
                    continue
                third = -keys[i] - keys[j]
                if third in dic:
                    if third < keys[j]:
                        continue
                    elif third > keys[j]:
                        ans.append([keys[i], keys[j], third])
                    elif third == keys[i]:
                        if dic[third] >= 3:
                            ans.append([keys[i], keys[j], third])
                    elif third == keys[j]:
                        if dic[third] >= 2:
                            ans.append([keys[i], keys[j], third])
                    else:
                        ans.append([keys[i], keys[j], third])
        return ans                