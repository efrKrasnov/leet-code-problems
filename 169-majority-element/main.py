class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        element = 0
        count = 0
        
        for i in range(len(nums)):
            if count == 0:
                element = nums[i]
                count += 1
            elif nums[i] == element:
                count += 1
            else:
                count -= 1
                
        return element