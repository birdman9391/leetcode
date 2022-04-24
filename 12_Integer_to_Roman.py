class Solution:
    def intToRoman(self, num: int) -> str:
        ret = ""
        first = num // 1000
        ret += self.write_symbol(first, "M", "", "")
        num %= 1000
        # return ret
        second = num // 100
        num %= 100
        ret += self.write_symbol(second, "C", "D", "M")
        
        third = num // 10
        num %= 10
        ret += self.write_symbol(third, "X", "L", "C")
        # return ret
        fourth = num
        ret += self.write_symbol(fourth, "I", "V", "X")
        
        return ret
    def write_symbol(self, count, cur, mid, prev):
        ret = ""
        if count in [4, 9]:
            count += 1
            ret += cur
        
        if count < 5:
            ret += cur*count
        elif count == 10:
            ret += prev
        else:
            ret += mid + (cur * (count - 5))
        return ret