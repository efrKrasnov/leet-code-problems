class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cur_pos = 0
        cur_item = -10001
        is_two_items = False
        
        for i in range(len(nums)):
            if cur_item != nums[i]:
                cur_item = nums[i]
                nums[cur_pos] = cur_item
                cur_pos += 1
                is_two_items = False
            else:
                if not is_two_items:
                    nums[cur_pos] = cur_item
                    cur_pos += 1
                    is_two_items = True
                    
        return cur_pos