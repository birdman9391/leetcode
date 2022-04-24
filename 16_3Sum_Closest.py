class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)-2):
            print(i, ans)
            if i>0 and nums[i-1] == nums[i]:
                continue
            minsum = nums[i] + nums[i+1] + nums[i+2]
            maxsum = nums[i] + nums[-1] + nums[-2]
            if minsum >= target:
                if abs(minsum-target) >= abs(ans-target):
                    return ans
            if maxsum < target:
                if abs(maxsum-target) < abs(ans-target):
                    ans = maxsum
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                thsum = nums[i] + nums[left] + nums[right]
                # print(thsum)
                if abs(thsum - target) < abs(ans - target):
                    ans = thsum
                if thsum == target:
                    return thsum
                elif thsum < target:
                    left += 1
                    while left < len(nums)-1 and nums[left-1] == nums[left]:
                        left += 1
                else:
                    right -= 1
                    while right > i and nums[right+1] == nums[right]:
                        right -= 1
        return ans