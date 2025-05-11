class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1: dict = {}
        m2: dict = {}
        for s_c, t_c in zip(s, t):
            mv = m1.get(s_c)
            if mv:
                if mv != t_c:
                    return False
            else:
                m1[s_c] = t_c
                
            mv = m2.get(t_c)
            if mv:
                if mv != s_c:
                    return False
            else:
                m2[t_c] = s_c
                    
        return True