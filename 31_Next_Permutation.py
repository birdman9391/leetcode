class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = -1

        for i in range(len(nums) - 1, -1, -1):
            if prev <= nums[i]:
                prev = nums[i]
                continue
            else:
                print(i)
                for j in range(i+1, len(nums)):
                    if nums[i] >= nums[j]:
                        nums[i], nums[j-1] = nums[j-1], nums[i]
                        break
                else:
                    nums[i], nums[len(nums)-1] = nums[len(nums)-1], nums[i]
                print(nums)
                head, tail = i+1, len(nums)-1
                while head < tail:
                    nums[head], nums[tail] = nums[tail], nums[head]
                    head += 1
                    tail -= 1
                break
        else:
            head, tail = 0, len(nums)-1
            while head < tail:
                nums[head], nums[tail] = nums[tail], nums[head]
                head += 1
                tail -= 1
            