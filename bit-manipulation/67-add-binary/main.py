class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """ Реализация двоичного сумматора (так как мы работаем в рамках двоичных вычислений)"""
        result = [""] * (max(len(a), len(b)) + 1)
        res_pos = len(result) - 1
        
        a_pos = len(a) - 1
        b_pos = len(b) - 1
        
        codes = {
            '0': 0,
            '1': 1
        }
        chars = ['0', '1']
        carry = 0
        while a_pos >= 0 or b_pos >= 0:
            partial_sum, carry = self.fullAdder(
                codes[a[a_pos]] if a_pos >= 0 else 0, 
                codes[b[b_pos]] if b_pos >= 0 else 0, 
                carry
            )
            result[res_pos] = chars[partial_sum]
            res_pos -= 1
            a_pos -= 1
            b_pos -= 1
        if carry:
            result[res_pos] = chars[carry]
            
        if not result[0]:
            return "".join(result[1:])
        else:
            return "".join(result)
    
    def fullAdder(self, a: int, b: int, carry: int) -> tuple[int, int]:
        x1 = a ^ b
        x2 = a & b
        y1 = carry ^ x1
        y2 = carry & x1
        z = y2 | x2
        return y1, z
        
        