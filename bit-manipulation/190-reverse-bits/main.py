class Solution:
    def reverseBits(self, n: int) -> int:
        n = n
        times = 16
        i = 0
        while times > 0:
            left_bit_pos = 15 + times
            right_bit_pos = 16 - times
            if ((n >> left_bit_pos) & 0b1) ^ ((n >> right_bit_pos) & 0b1):
                mask = (1 << left_bit_pos) | (1 << right_bit_pos)
                n ^= mask
            times -= 1
            i += 1
        return n
    
    
if __name__ == "__main__":
    s = Solution()
    assert s.reverseBits(43261596) == 964176192