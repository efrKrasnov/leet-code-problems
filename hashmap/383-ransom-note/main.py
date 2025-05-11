class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        LETTERS_COUNT = 26
        rnl = [0] * LETTERS_COUNT
        ml = [0] * LETTERS_COUNT
        
        for c in ransomNote:
            rnl[ord(c) - 97] += 1 
            
        for c in magazine:
            ml[ord(c) - 97] += 1
            
        for i in range(LETTERS_COUNT):
            if ml[i] - rnl[i] < 0:
                return False
        return True