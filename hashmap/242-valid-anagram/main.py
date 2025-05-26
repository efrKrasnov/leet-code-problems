class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freqs = {}
        
        for c in s:
            if c not in s_freqs:
                s_freqs[c] = 1
            else:
                s_freqs[c] += 1
                
        for c in t:
            if c not in s_freqs:
                s_freqs[c] = -1
            else:
                s_freqs[c] -= 1
                
        return not any(s_freqs.values())