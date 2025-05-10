class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        insert_idx = 0
        for i in range(len(nums)):
            if nums[i] == val:
                insert_idx += 1
            else:
                nums[i - insert_idx] = nums[i]

        return len(nums) - insert_idx
