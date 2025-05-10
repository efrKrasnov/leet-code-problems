class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1 = 0
        ptr2 = len(s) - 1
        
        while True:
            while ptr1 < len(s) and not self.is_char(s[ptr1]):
                ptr1 += 1
            while ptr2 > -1 and not self.is_char(s[ptr2]):
                ptr2 -= 1
                
            if ptr1 >= ptr2:
                return True
            else:
                if s[ptr1].lower() != s[ptr2].lower():
                    return False
                ptr1 += 1
                ptr2 -= 1
            
    def is_char(self, letter: str):
        code = ord(letter.lower())
        return (code >= 97 and code <= 122) or (code >= 48 and code <= 57)