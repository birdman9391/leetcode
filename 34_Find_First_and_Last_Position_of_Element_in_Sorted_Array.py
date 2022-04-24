class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, head, tail, target):
            mid = (head + tail) // 2
            print(nums, head, mid, tail, target)
            if tail == head:
                return [-1, -1]
            if tail - head == 1:
                if nums[head] == target:
                    return [head, head + 1]
                else:
                    return [-1, -1]
            
            
            ret = [-1, -1]
            
            if nums[mid] == target:
                ret = [mid, mid + 1]
                if nums[head] == target:
                    ret[0] = head
                if nums[tail - 1] == target:
                    ret[1] = tail
                
                if ret[0] != head:
                    ret_2 = binary_search(nums, head, mid, target)
                    ret[0] = ret_2[0] if ret_2[0] != -1 else ret[0]
                    
                if ret[1] != tail:
                    ret_2 = binary_search(nums, mid + 1, tail, target)
                    ret[1] = ret_2[1] if ret_2[1] != -1 else ret[1]
                return ret

            if nums[mid] > target:
                return binary_search(nums, head, mid, target)
            else:
                return binary_search(nums, mid + 1, tail, target)
        ret = binary_search(nums, 0, len(nums), target)
        if ret[1] != -1:
            ret[1] -= 1
        return ret