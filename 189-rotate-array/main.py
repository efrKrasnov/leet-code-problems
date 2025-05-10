class Solution:
    def rotate(self, nums: list[int | None], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        if k == 0:
            return

        i = len(nums) - 1
        j = i - k

        temp = nums[i]
        nums[i] = None
        times = k
        is_shift_required = len(nums) % k == 0
        while times:
            nums[i] = nums[j]
            nums[j] = None
            i = j
            j -= k
            if j < 0:
                j += len(nums)
                times -= 1
                if is_shift_required:
                    nums[i] = temp
                    i = j - 1
                    j -= (k + 1)
                    temp = nums[i]
                    nums[i] = None
        nums[i] = temp
                    
            
