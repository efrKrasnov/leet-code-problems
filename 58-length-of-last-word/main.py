class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        is_stripped = False
        length = 0
        for c in reversed(s):
            if c == ' ':
                if not is_stripped:
                    continue
                else:
                    break
            else:
                is_stripped = True
                length += 1
                
        return length