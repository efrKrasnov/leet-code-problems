class Solution:
    def hammingWeight(self, n: int) -> int:
        ones_count = 0
        while n:
            n &= (n - 1)
            ones_count += 1
        return ones_count