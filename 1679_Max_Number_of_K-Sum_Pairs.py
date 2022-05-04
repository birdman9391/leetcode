class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        myDict = dict()
        answer = 0
        for num in nums:
            k_num = k - num
            try:
                myDict[k_num] -= 1
                answer += 1
                if not myDict[k_num]:
                    del myDict[k_num]
            except:
                try:
                    myDict[num] += 1
                except:
                    myDict[num] = 1
        return answer