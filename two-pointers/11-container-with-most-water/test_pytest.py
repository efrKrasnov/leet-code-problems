from main import Solution


def test_1():
    s = Solution()
    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    
    
def test_2():
    s = Solution()
    assert s.maxArea([1,1]) == 1
    