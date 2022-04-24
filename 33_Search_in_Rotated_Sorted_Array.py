class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, head, tail, target):
            print(nums, head, tail, target)
            if tail - head == 0:
                return -1
            elif tail - head == 1:
                if nums[head] == target:
                    return head
                else:
                    return -1
            else:
                mid = (head + tail) // 2
                # head_is_sorted 
                if nums[head] <= nums[mid - 1]:
                    if nums[head] <= target <= nums[mid - 1]:
                        return binary_search(nums, head, mid, target)
                    else:
                        return binary_search(nums, mid, tail, target)
                else:
                    if nums[mid] <= target <= nums[tail - 1]:
                        return binary_search(nums, mid, tail, target)
                    else:
                        return binary_search(nums, head, mid, target)
        return binary_search(nums, 0, len(nums), target)