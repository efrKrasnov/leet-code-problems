class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_pos = m + n - 1
        n -= 1
        m -= 1
        while n >= 0:
            if m < 0 or nums1[m] <= nums2[n]:
                nums1[insert_pos] = nums2[n]
                n -= 1
            else:
                nums1[insert_pos] = nums1[m]
                m -= 1
            insert_pos -= 1
