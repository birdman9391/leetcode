class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        is_minus = str_x[0] == "-"
        if is_minus:
            str_x = str_x[1:]
        reversed_str_x = str_x[::-1]
        reversed_x = int(reversed_str_x)
        if is_minus:
            reversed_x *= -1
        if reversed_x not in range(-pow(2, 31), pow(2, 31)):
            return 0
        else:
            return reversed_x