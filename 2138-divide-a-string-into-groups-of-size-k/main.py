class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        chars_remain = len(s) % k
        if chars_remain:
            s = s + (fill * (k - chars_remain))
        i = 0
        result = []
        while i < len(s):
            result.append(s[i: i + k])
            i += k
        return result
    