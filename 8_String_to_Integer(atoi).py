class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] == '+':
            is_positive = 1
            s = s[1:]
        elif s[0] == '-':
            is_positive = -1
            s = s[1:]
        else:
            is_positive = 1
            
        for i, c in enumerate(s):
            if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                s = s[:i]

        for i, c in enumerate(s):
            if c != '0':
                s = s[i:]
                break
            if i == len(s) - 1:
                return 0

        if len(s) == 0:
            return 0
            
            
        if len(s) > 10:
            if is_positive == 1:
                return 2**31 - 1
            else:
                return - 2**31
        elif len(s) < 10:
            return is_positive * int(s)
        else:
            if is_positive == 1:
                return min(int(s), 2**31 - 1)
            else:
                return max(-int(s), - 2**31)
            