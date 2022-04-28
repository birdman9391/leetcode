class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cnt = 0
        cur_pos = 0
        max_jump = 0
        max_pos = 0
        if len(nums) == 1:
            return True
        while True:
            cnt += 1
            if cur_pos + nums[cur_pos] >= len(nums) - 1:
                return True
            for i in range(cur_pos + 1, cur_pos + nums[cur_pos] + 1):
                jump_range = i + nums[i]
                if jump_range > max_jump:
                    max_pos = i
                    max_jump = jump_range
            if cur_pos == max_pos:
                return False
            cur_pos = max_pos