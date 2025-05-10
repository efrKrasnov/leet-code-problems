from main import Solution


def test_1():
    s = Solution()
    assert s.majorityElement([3,2,3])
    
    
def test_2():
    s = Solution()
    assert s.majorityElement([2,2,1,1,1,2,2])