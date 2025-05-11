from main import Solution


def test_1():
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]
    
    
def test_2():
    s = Solution()
    nums1 = [1]
    m = 1
    nums2: list[int] = []
    n = 0
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1]
    
    
def test_3():
    s = Solution()
    nums1 = [0]
    m = 0
    nums2: list[int] = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1]
    
    
def test_4():
    s = Solution()
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,3,4,5,6]
