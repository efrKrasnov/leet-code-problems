class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:          
        s_pos = len(s) - 1
        t_pos = len(t) - 1
        
        if s_pos < 0:
            return True
        
        if t_pos < 0:
            return False
        
        while True:
            if s[s_pos] == t[t_pos]:
                s_pos -= 1
            t_pos -= 1
            if s_pos < 0  or t_pos < 0:
                break
            
        if s_pos < 0:
            return True
        else:
            return False

            