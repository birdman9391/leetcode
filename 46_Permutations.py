class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums.copy()]
        prev_permutation = self.permute(nums[1:])
        new_permutation = []
        for item in prev_permutation:
            l = len(item)
            for i in range(l + 1):
                new_item = item.copy()
                new_item.insert(i, nums[0])
                new_permutation.append(new_item)
                
        return new_permutation