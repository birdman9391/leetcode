class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        i, j, k, l = 0, 1, 2, 3
        nLen = len(nums)
        ret = []
        for i in range(nLen - 3):
            if 4 * nums[i] > target:
                break
            for l in range(i + 3, nLen):
                if nums[i] + nums[l-2] + nums[l-1] + nums[l] < target:
                    continue
                for k in range(i + 2, l):
                    if nums[i] + nums[l] + nums[k - 1] + nums[k] < target:
                        continue
                    if nums[i] + nums[l] + nums[i + 1] + nums[k] > target:
                        break
                    for j in range(i + 1, k):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            ret.append((nums[i], nums[j], nums[k], nums[l]))
                        elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                            break
        return list(set(ret))
