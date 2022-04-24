class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute(nums: List[int]) -> List[List[int]]:
            # print(nums)
            if len(nums) == 1:
                return [nums.copy()]
            prev_permutation = permute(nums[1:])
            new_permutation = []
            for item in prev_permutation:
                l = len(item)
                for i in range(l + 1):
                    new_item = item.copy()
                    new_item.insert(i, nums[0])
                    new_permutation.append(new_item)
                    if i < l and nums[0] == item[i]:
                        break

            # print(new_permutation)
            return new_permutation
        
        nums.sort()
        return permute(nums)
