from main import Solution


def test_1():
    s = Solution()
    assert s.twoSum([2,7,11,15], 9) == [1, 2]
    
    
def test_2():
    s = Solution()
    assert s.twoSum([2, 3, 4], 6) == [1, 3]
    
    
def test_3():
    s = Solution()
    assert s.twoSum([-1, 0], -1) == [1, 2]