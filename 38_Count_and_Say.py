class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev_str = self.countAndSay(n-1)
        cur_str = ""
        prev_ch = prev_str[0]
        cnt = 0
        for ch in prev_str:
            if cnt == 0:
                cnt += 1
                prev_ch = ch
            elif ch == prev_ch:
                cnt += 1
            else:
                cur_str += str(cnt) + prev_ch
                cnt = 1
                prev_ch = ch

            # print(n, cnt, ch, cur_str)
        if cnt != 0:
            cur_str += str(cnt) + prev_str[-1]
        # print(n, cur_str)
        return cur_str
                