class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        prev = -10e6
        for i, num in enumerate(nums):
            if prev > num:
                head = i - 1
                break
            prev = num
        else:
            return 0
        next = 10e6 
        for i, num in reversed(list(enumerate(nums))):
            if num > next:
                tail = i + 1
                break
            next = num
        else:
            return 0
        
        MIN, MAX = min(nums[head:tail+1]), max(nums[head:tail+1])
        
        for i, num in enumerate(nums[:head]):
            if num > MIN:
                head = i
                break
        for i, num in reversed(list(enumerate(nums))):
            if num < MAX:
                tail = i
                break
            elif i == tail:
                break

        return tail - head + 1
                