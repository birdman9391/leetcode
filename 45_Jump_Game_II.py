class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        cur_pos = 0
        max_jump = -1
        max_pos = -1
        if len(nums) == 1:
            return 0
        while True:
            cnt += 1
            if cur_pos + nums[cur_pos] >= len(nums) - 1:
                return cnt
            for i in range(cur_pos + 1, cur_pos + nums[cur_pos] + 1):
                jump_range = i + nums[i]
                if jump_range > max_jump:
                    max_pos = i
                    max_jump = jump_range
            cur_pos = max_pos