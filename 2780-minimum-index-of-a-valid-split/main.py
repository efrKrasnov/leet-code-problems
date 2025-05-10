class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        result = -1
        
        freqs: dict[int, int] = {}
        for n in nums:
            if n not in freqs:
                freqs[n] = 1
            else:
                freqs[n] += 1
        max_freq_key = 0
        max_freq_val = 0
        for n in freqs.keys():
            if max_freq_val < freqs[n]:
                max_freq_key = n
                max_freq_val = freqs[n]
        
        key_count = 0    
        for i in range(len(nums)):
            if nums[i] == max_freq_key:
                key_count += 1
            if key_count * 2 > i + 1:
                items_remain = len(nums) - (i + 1)
                freqs_remain = max_freq_val - key_count
                if freqs_remain * 2 > items_remain:
                    return i
        return result