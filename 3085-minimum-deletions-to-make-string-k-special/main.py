class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from collections import defaultdict
        
        freqs: dict[str, int] = defaultdict(int)
        for c in word:
            freqs[c] = freqs[c] + 1
            
        min_removes_count = 1000000
        for freq_i in freqs:
            removes_count = 0
            for freq_j in freqs:
                if freq_i == freq_j:
                    continue
                else:
                    if freqs[freq_j] < freqs[freq_i]:
                        removes_count += freqs[freq_j]
                    if freqs[freq_j] > freqs[freq_i] + k:
                        removes_count += freqs[freq_j] - (freqs[freq_i] + k)
                        
            if removes_count < min_removes_count:
                min_removes_count = removes_count            
            
        return min_removes_count
    