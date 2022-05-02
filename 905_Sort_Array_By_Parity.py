class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        head, tail = 0, len(nums) - 1
        
        while True:
            while head < tail and not nums[head] % 2:
                head += 1
            while head < tail and nums[tail] % 2:
                tail -= 1
            if head < tail:
                nums[head], nums[tail] = nums[tail], nums[head]
            else:
                break
                
        return nums