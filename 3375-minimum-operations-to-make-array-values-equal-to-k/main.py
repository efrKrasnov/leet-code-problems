class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        result = set()
        is_equal = False
        
        for i in range(len(nums)):
            if nums[i] > k:
                result.add(nums[i])
            elif nums[i] == k:
                is_equal = True
            else:
                return -1
                
        result_len = len(result)
        if result_len > 0:
            return result_len
        else:
            if is_equal:
                return 0
            else:
                return -1