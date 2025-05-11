class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:       
        lo = 0
        hi = len(numbers) - 1
        
        while True:
            sum = numbers[lo] + numbers[hi]
            if sum > target:
                hi -= 1
            elif sum < target:
                lo += 1
            else:
                return [lo + 1, hi + 1]
        
        
        